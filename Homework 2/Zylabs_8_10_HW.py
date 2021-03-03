# Lorenzo Gonzales
# ID: 1934789
# Palindrome
Palindrome = input()
word = ""
for i in Palindrome:
    word = i + word
if Palindrome == word:
    print(Palindrome, 'is a palindrome')  # If its a palindrome its messaged here
else:
    print(Palindrome, 'is not a palindrome')  # If not then this message comes up

