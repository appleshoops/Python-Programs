import math

word = input('Enter a word: ')
length = len(word)
loopTimes = math.floor(length / 2)
isPalindrome = True

for i in range(loopTimes):
    if word[i] != word[-i-1]: # -1 is the last value for an array
        isPalindrome = False
        break

if isPalindrome == True:
    print(f'{word} is a palindrome')
else:
    print(f'{word} is not a palindrome')

    