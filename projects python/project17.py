#esse sari detail aa jayegi jiska gmail he uski 

from skpy import Skype

slogin = Skype("yaha gmail likhna h","yaha password")

contact = slogin.contacts

for i in contact:
    print(i)
