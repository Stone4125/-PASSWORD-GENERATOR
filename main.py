import random

letters = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','$','%','^','&','*','(',')','_','+']

print ("WELCOME TO YHE PASSWORD GENERATOR")
nr_letters = int (input("How many letters would you like in your password?"))
nr_numbers = int (input("How many numbers would you like in your password?"))
nr_symbols = int (input("How many symbols would you like in your password?"))
password = []
for i in range (nr_letters) :
  choix1 = random.choice(letters)
  password += choix1
for n in range (nr_numbers) :
  choix2 = random.choice(numbers)
  password += choix2
for m in range (nr_symbols) :
  choix3 = random.choice(symbols)
  password += choix3
random.shuffle(password)   #melange les elements de la liste password
password_str = "".join(password) #transforme la liste en chaine de caractere
print (f"Votre mot de passe est : {password_str}")