import random
num_letters = int(input('How many letters should it has: '))
num_symbols = int(input('How many symbols should it has: '))
num_numbers = int(input('How many numbers should it has: '))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['$', '%', '@', '#', '&', '*']
numbers = [0,1,2,3,4,5,6,7,8,9]

password_letter = []
password_symbol = []
password_number = []
x = 0
y = 0
z = 0

upperLetter = []
for item in letters:
  upperLetter.append(item.upper())



#for num_letters in letters:
while x < num_letters:
  if x % 2 == 0:
    password_letter.append(random.choice(letters))
  else:
    password_letter.append(random.choice(upperLetter))
  x += 1

while y < num_symbols:
  password_symbol.append(random.choice(symbols))
  y += 1

while z < num_numbers:
  password_number.append(str(random.choice(numbers)))
  z += 1
  

password = password_letter + password_symbol + password_number
random.shuffle(password)
password = "".join(password)

print(password)

