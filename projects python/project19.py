import smtplib as s

ob = s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('yaha gmail','yaha pass')
sub = "test python"
body = "I Love Python"
msg = "sub:{}\n\n{}".format(sub,body)
listadd = ['biggbosslive670@gmail.com']
ob.sendmail('yaha bhi vahi gmail',listadd,msg)
print("Done")
ob.quit()