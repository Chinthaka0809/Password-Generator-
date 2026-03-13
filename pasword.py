import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to password Genarator..")

in_letters = int(input("How many latters would you like in your password : "))

in_symbols = int(input("How many Symbol would you like in your password : "))

in_numbers = int(input("How many numbers would you like in your password : "))


password = ""
for lette in range(1, in_letters +1):
    password += random.choice(letters)

for sym in range(1, in_symbols +1):
    password += random.choice(symbols)

for num in range(1, in_numbers +1):
    password += random.choice(numbers)

print("Easy level pasword : "  + password)

h_password = []
f_password = ""

for i in password:
        h_password.append(i)

random.shuffle(h_password)
for x in h_password:
    f_password += x
    
# for x in h_password:
#      f_password += random.choice(h_password)
      
print("Hard Level Password : "+f_password)

# age = [22,55,24,76,11,34]
# random.shuffle(age)
# print(age)
