# name = "Harsh"
# print(name)
# print(len(name))
# print(name[1:3])
# print(name.count("H"))

# num = int(input("enter a number: "))
# print(num + 6)

# t = (1, 2, 4, 5)
# #tupple ko change nhi kar skte
# #pop mtlb koi bhi random variable hata dega
# a = { }
# print(type(a))

# a = 2

# match a:
#     case 1:
#         print("kahe aaye ho")

#     case 2:
#         print("case 2 h")    


# for i in range(101):
#     print(i)

# i = 1

# while(i<100):
#     print(i)
#     i +=1

# while(True):
#     num = int(input("Enter number: "))
#     print(num)
#     if(num == 19):
#         break

# print("ab bas hogaya")

##FUNCTIONS

# def Microsoft(name, occupation):
#     s = f"Hey my name is {name} and i am a {occupation} "
#     print(s)

# Microsoft("Harsh Jangid", "Data Scientist")


# #try se error nhi ayega
# try:
#     a = int(input("Enter number: "))
#     print(a)
# except Exception as e:
#     print("Some error occurred: ",e)

# s = "Use for your 1st project"

# with open("Project.txt", "w") as f:
#     f.write(s)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

a = Employee("Harsh", "25LPA")
print(a.name)
print(a.salary)






