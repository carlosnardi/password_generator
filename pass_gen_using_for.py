import random
num_letters = int(input('How many letters should it have: '))
num_symbols = int(input('How many symbols should it have: '))
num_numbers = int(input('How many numbers should it have: '))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['$', '%', '@', '#', '&', '*']
numbers = [0,1,2,3,4,5,6,7,8,9]

password_letter = []
password_symbol = []
password_number = []

letters_upper = []
for letter in letters:
  letters_upper.append(letter.upper())


letters_list = []
x = num_letters 
for char in range(0,num_letters):
  if x % 2 == 0:
    letters_list.append(random.choice(letters))
  else:
    letters_list.append(random.choice(letters_upper))
  x -= 1

for sym in range(0,num_symbols):
  password_symbol.append(random.choice(symbols))

for num in range(0,num_numbers):
  password_number.append(random.choice(numbers))


password_list = letters_list + password_symbol + password_number 

random.shuffle(password_list)

password = ""
for item in password_list:
  password += str(item)

print(password)
  
  
