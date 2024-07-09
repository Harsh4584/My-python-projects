import phonenumbers
from phonenumbers import timezone,geocoder,carrier
num = input("Enter Your Number with +__: ")
phone=phonenumbers.parse(num)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,"en")
reg=geocoder.description_for_number(phone,"en")
print(phone)
print(time)
print(car)
print(reg)


# ye error aise hi show hora h code chal rha h ache se















