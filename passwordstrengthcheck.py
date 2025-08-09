import string
from colorama import Fore, Style, init

init(autoreset=True)


password = input("Enter a password: ")

score = 0

if len(password) >= 8:
    score += 1

if any(char.isupper() for char in password):
    score += 1

if any(char.islower() for char in password):
    score += 1

if any(char.isdigit() for char in password):
    score += 1

if any(char in string.punctuation for char in password):
    score += 1

if score <= 2:
    print(Fore.RED + "Password strength: Weak")
elif score <= 4:
    print(Fore.YELLOW + "Password strength: Medium")
else:
    print(Fore.GREEN + "Password strength: Strong")


