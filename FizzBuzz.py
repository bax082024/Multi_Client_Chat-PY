from colorama import Fore, Style, init

init(autoreset=True)

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print(Fore.YELLOW + "FizzBuzz")
    elif num % 3 == 0:
        print(Fore.GREEN + "Fizz")
    elif num % 5 == 0:
        print(Fore.CYAN + "Buzz")
    else:
        print(Style.RESET_ALL + str(num))
