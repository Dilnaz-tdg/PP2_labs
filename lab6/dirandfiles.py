import os

path = r'C:\Users\Aspire 3\Desktop\PP2_labs\lab3'

#1
# только файлы
for entry in os.listdir():
    if os.path.isfile(entry):
        print(entry)

print("------")

# только dir
for entry in os.listdir():
    if os.path.isdir(entry):
        print(entry)


print("------")
# все вместе
for entry in os.listdir():
    print(entry)

print("------")
# только файлы в спец path
for entry in os.listdir(path):
    full_path = os.path.join(path, entry) 

    if os.path.isfile(full_path):
        print(entry)


#2
path = r'C:\Users\Aspire 3\Desktop\PP2_labs\lab2'

if (os.access(path, os.F_OK)):
    print("Existence: true")
else:
    print("Existence: false")

if (os.access(path, os.R_OK)):
    print("Readability: true")
else:
    print("Readability: false")

if (os.access(path, os.W_OK)):
    print("Writability: true")
else:
    print("Writability: false")

if (os.access(path, os.X_OK)):
    print("Executability: true")
else:
    print("Executability: false")

#3
if os.path.exists(path):
    print("path is exists")
    print(os.path.basename(path))
    print(os.path.dirname(path))
else:
    print("path is not exists")


#4
file_name = 'text.txt'
file = open(file_name)

lines_list = list(file)

print('Length:' , len(lines_list))


#5 
mylist = ["hello", "this", "is", "list"]
with open("text.txt", "w") as file:
   for item in mylist:
    file.write(item + "\n")


#6
import string
uppercase_alphabet = string.ascii_uppercase
for letter in uppercase_alphabet:
    filename = f"{letter}.txt"
    with open(filename, "w") as file:
        file.write(f"This is {letter}.txt file")

#7
with open("text.txt", "r") as rf:
   with open("text_copy.txt", "w") as wf:
       for line in rf:
           wf.write(line)

#8

path = r'C:\Users\Aspire 3\Desktop\PP2_labs\lab6\filetext.txt'
filetodel = 'filetext.txt'
if os.path.exists(path) and (os.access(path, os.W_OK)):
    os.remove(path)

