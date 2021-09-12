import random
print("Welcome to the Password generator")
chars = 'azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN1230456789'
number = int(input('Number of passwords to generate: '))
length = int(input('Input your password length: '))
print('\n here are your passwords: ')
for pwd in range(number):
    passwords = ' '
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)