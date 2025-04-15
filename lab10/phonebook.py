import psycopg2
import csv

def connect():
    conn = psycopg2.connect(
    host="localhost",
    port=5433,
    database="postgres",
    user="postgres",
    password="12345"
)
    return conn

def insert_from_console():
    conn = connect()
    cur = conn.cursor()
    first_name = input("Enter name: ")
    phone = input("Enter phone: ")
    cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (first_name, phone))
    conn.commit()
    
   
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    print("Current data in phonebook:")
    for row in rows:
        print(row)

    cur.close()
    conn.close()


def insert_from_csv(filename):
    conn = connect()
    cur = conn.cursor()
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (row['first_name'], row['phone']))
    conn.commit()
    cur.close()
    conn.close()

def update_user(name, new_phone):
    conn = connect()
    cur = conn.cursor()
    cur.execute("UPDATE phonebook SET phone = %s WHERE first_name = %s", (new_phone, name))
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

    rows = cur.fetchall()
    
    print(f"Найдено записей: {len(rows)}")
    
    if not rows:
        print("No results found.")
    else:
        for row in rows:
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



while True:
    print("\nPHONEBOOK MENU")
    print("1. Insert from console")
    print("2. Insert from CSV")
    print("3. Update user")
    print("4. Search")
    print("5. Delete")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        insert_from_console()
    elif choice == "2":
        insert_from_csv("phonebook.csv")
    elif choice == "3":
        name = input("Enter name to update: ")
        new_phone = input("Enter new phone: ")
        update_user(name, new_phone)
    elif choice == "4":
        filter_by = input("Search by (name/phone/all): ").lower()
        if filter_by == "name":
            name = input("Enter name: ")
            search(name=name)
        elif filter_by == "phone":
            phone = input("Enter phone: ")
            search(phone=phone)
        else:
            search()
    elif choice == "5":
        delete_by = input("Delete by (name/phone): ").lower()
        if delete_by == "name":
            name = input("Enter name to delete: ")
            delete(name=name)
        else:
            phone = input("Enter phone to delete: ")
            delete(phone=phone)
    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
    
