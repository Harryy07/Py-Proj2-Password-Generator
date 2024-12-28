import random
from typing import final

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = [] #created an empty list to store all the new items from above list.

for i in range(1, nr_letters + 1):      #the range will check between 1 and user's input + 1 keeping in mind inclusivity
    password_list.append(random.choice(letters)) #adding the randomly chosen letter in the list as an item

for i in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

for i in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list) #shuffle the list items.
final_password = ""           # created to hold the new set of final password
for p in password_list:
    final_password += p

print(final_password)

