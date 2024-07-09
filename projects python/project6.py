# ? kahta h ki jo "." or "_" hai vo ek baar hi hone chahiye email me in regex
while True:
    import re
    email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
    user_email = input("Enter your Email: ")

    if re.search(email_condition,user_email):
        print("Right Email")
    else:
        print("Wrong Email")

 




























