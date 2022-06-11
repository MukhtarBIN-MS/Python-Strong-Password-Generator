import random 

import time

print("Welcome to Srtong password generator")

alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
signs =['@','#','$','%','^','&','*','(',')','_','+']
numbers = ['1','2','3','4','5','6','7','8','9','0']


def password_generator(letter, sign, number):

    letter = int(input("How many letter do you want in your password ?? "))
    sign = int(input("How many sign do you want in your passwords ? "))
    number = int(input("How many numbers do you want ?? "))

    password_list = []

    for char in range(1, letter + 1):
        password_list.append(random.choice(alphabets))

    for char in range(1, sign + 1):
        password_list.append(random.choice(signs))

    for char in range(1, number + 1):
        password_list.append(random.choice(numbers))

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    print(f"Your storg password is {password}")

password_generator(2,2,2)