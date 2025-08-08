user_input = input("Enter numbers seperated by spaces: ")

numbers = [int(x) for x in user_input.split()]

largest= numbers[0]

for num in numbers:
  if num > largest:
    largest = num 

print("The largest number is: ", largest)