import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Py-ssword Suggestor!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

total_len = nr_letters + nr_symbols + nr_numbers
what_type = random.randint(0,2)

password = ''

for i in range(nr_letters):
    password = password + letters[random.randint(0,len(letters)-1)]
    
for i in range(nr_symbols):
    password = password + symbols[random.randint(0,len(symbols)-1)]
    
for i in range(nr_numbers):
    password = password + numbers[random.randint(0,len(numbers)-1)]

better = []

for i in password:
    better.append(password[random.randint(0, len(password)-1)])
    
print(''.join(better))
