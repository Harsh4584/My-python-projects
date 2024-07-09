pwd = input("What is the pro password? ")

def view():
    file = open('passwords.txt', 'r') 
    file.close()
    for line in file.readlines():
        print(line)
    

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    file = open('passwords.txt', 'a') 
    file.close()
    file.write(name + "|" + pwd + "\n")


mode = input("Would you like to add a new password or view existing ones (view, add)? ")
while True:
    if mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode == "q":
        break
    else:
        print("Invalid mode")
        continue
    