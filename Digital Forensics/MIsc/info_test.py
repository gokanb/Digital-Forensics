from faker import Faker
from random import Random

info = Faker()

print(info.name())


print(info.address())


for i in range(1, 21):
    print(info.name()) 

#for i in range(1, 25):
    print(f'["{i}", "{info.name()}", "Mobile", "{info.date()}{info.time()}", "{randit(0, 100)}"]')