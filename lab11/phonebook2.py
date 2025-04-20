import psycopg2
import csv

def connect():
    return psycopg2.connect(
        host="localhost",
        port=5433,
        database="postgres",
        user="postgres",
        password="12345"
    )

def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(255),
            phone VARCHAR(20)
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

def init_procedures():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE OR REPLACE FUNCTION search_by_pattern(pattern TEXT)
    RETURNS TABLE(id INT, first_name TEXT, phone TEXT) AS $$
    BEGIN
        RETURN QUERY
        SELECT phonebook.id, phonebook.first_name::TEXT, phonebook.phone::TEXT
        FROM phonebook
        WHERE phonebook.first_name ILIKE '%' || pattern || '%'
           OR phonebook.phone ILIKE '%' || pattern || '%';
    END;
    $$ LANGUAGE plpgsql;
    """)

    cur.execute("""
    CREATE OR REPLACE PROCEDURE insert_or_update_user(p_name TEXT, p_phone TEXT)
    AS $$
    BEGIN
        IF EXISTS (SELECT 1 FROM phonebook WHERE first_name = p_name) THEN
            UPDATE phonebook SET phone = p_phone WHERE first_name = p_name;
        ELSE
            INSERT INTO phonebook(first_name, phone) VALUES (p_name, p_phone);
        END IF;
    END;
    $$ LANGUAGE plpgsql;
    """)

    cur.execute("""
    CREATE OR REPLACE FUNCTION insert_many_users(
        names TEXT[],
        phones TEXT[]
    )
    RETURNS TEXT[] AS $$
    DECLARE
        i INT := 1;
        invalid_data TEXT[] := ARRAY[]::TEXT[];
    BEGIN
        WHILE i <= array_length(names, 1) LOOP
            IF phones[i] ~ '^\\+?[0-9]{5,15}$' THEN
                CALL insert_or_update_user(names[i], phones[i]);
            ELSE
                invalid_data := array_append(invalid_data, names[i] ':' phones[i]);
            END IF;
            i := i + 1;
        END LOOP;
        RETURN invalid_data;
    END;
    $$ LANGUAGE plpgsql;
    """)

    cur.execute("""
    CREATE OR REPLACE FUNCTION pagination(p_limit INT, p_offset INT)
    RETURNS TABLE(id INT, first_name TEXT, phone TEXT) AS $$
    BEGIN
        RETURN QUERY
        SELECT phonebook.id, phonebook.first_name::TEXT, phonebook.phone::TEXT
        FROM phonebook
        ORDER BY id LIMIT p_limit OFFSET p_offset;
    END;
    $$ LANGUAGE plpgsql;
    """)

    cur.execute("""
    CREATE OR REPLACE PROCEDURE delete_user(p_name TEXT DEFAULT NULL, p_phone TEXT DEFAULT NULL)
    AS $$
    BEGIN
        IF p_name IS NOT NULL THEN
            DELETE FROM phonebook WHERE first_name = p_name;
        ELSIF p_phone IS NOT NULL THEN
            DELETE FROM phonebook WHERE phone = p_phone;
        END IF;
    END;
    $$ LANGUAGE plpgsql;
    """)

    conn.commit()
    cur.close()
    conn.close()


def insert_from_console():
    conn = connect()
    cur = conn.cursor()
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()

def insert_from_csv(filename):
    conn = connect()
    cur = conn.cursor()
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (row['first_name'], row['phone']))
    conn.commit()
    cur.close()
    conn.close()

def update_user(name, phone):
    conn = connect()
    cur = conn.cursor()
    cur.execute("UPDATE phonebook SET phone = %s WHERE first_name = %s", (phone, name))
    conn.commit()
    cur.close()
    conn.close()

def search(name=None, phone=None):
    conn = connect()
    cur = conn.cursor()
    if name:
        cur.execute("SELECT * FROM phonebook WHERE first_name ILIKE %s", (f"%{name}%",))
    elif phone:
        cur.execute("SELECT * FROM phonebook WHERE phone ILIKE %s", (f"%{phone}%",))
    else:
        cur.execute("SELECT * FROM phonebook")
    for row in cur.fetchall():
        print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]}")
    cur.close()
    conn.close()

def delete(name=None, phone=None):
    conn = connect()
    cur = conn.cursor()
    if name:
        cur.execute("DELETE FROM phonebook WHERE first_name = %s", (name,))
    elif phone:
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
    conn.commit()
    cur.close()
    conn.close()

def search_by_pattern(pattern):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM search_by_pattern(%s)", (pattern,))
    for row in cur.fetchall():
        print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]}")
    cur.close()
    conn.close()

def insert_or_update(name, phone):
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()

def insert_many(names, phones):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT insert_many_users(%s, %s)", (names, phones))
    invalid = cur.fetchone()[0]
    if invalid:
        print("Invalid data:", invalid)
    else:
        print("data inserted successfully.")
    conn.commit()
    cur.close()
    conn.close()

def paginate(limit, offset):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM pagination(%s, %s)", (limit, offset))
    for row in cur.fetchall():
        print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]}")
    cur.close()
    conn.close()

def delete_proc(name=None, phone=None):
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL delete_user(%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()
create_table()
init_procedures()

while True:
    print("\nPHONEBOOK MENU")
    print("1. Insert from console")
    print("2. Insert from CSV")
    print("3. Update user")
    print("4. Search")
    print("5. Delete")
    print("6. Search by pattern (stored function)")
    print("7. Insert/update (stored procedure)")
    print("8. Insert many (stored function)")
    print("9. Paginate (stored function)")
    print("10. Delete (stored procedure)")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        insert_from_console()
    elif choice == "2":
        insert_from_csv("phonebook.csv")
    elif choice == "3":
        update_user(input("Name: "), input("New phone: "))
    elif choice == "4":
        mode = input("Search by (name/phone/all): ").lower()
        if mode == "name":
            search(name=input("Enter name: "))
        elif mode == "phone":
            search(phone=input("Enter phone: "))
        else:
            search()
    elif choice == "5":
        mode = input("Delete by (name/phone): ").lower()
        if mode == "name":
            delete(name=input("Enter name: "))
        else:
            delete(phone=input("Enter phone: "))
    elif choice == "6":
        search_by_pattern(input("Enter pattern: "))
    elif choice == "7":
        insert_or_update(input("Enter name: "), input("Enter phone: "))
    elif choice == "8":
        n = int(input("How many users to add? "))
        names, phones = [], []
        for i in range(n):
            names.append(input(f"Name {i+1}: "))
            phones.append(input(f"Phone {i+1}: "))
        insert_many(names, phones)
    elif choice == "9":
        paginate(int(input("Limit: ")), int(input("Offset: ")))
    elif choice == "10":
        mode = input("Delete by (name/phone): ").lower()
        if mode == "name":
            delete_proc(name=input("Enter name: "))
        else:
            delete_proc(phone=input("Enter phone: "))
    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
