word = input("Enter a word: ")

reversed_word = ""

for letter in word[::-1]:
  reversed_word += letter

print ("Reversed word : ", reversed_word)