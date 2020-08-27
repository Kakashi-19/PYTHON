import re
# program for counting vowels in a string

print('Enter a Word Or Sentence')
word = input()
vowelRegex = re.compile(r'[aeiou]')
vowels = vowelRegex.findall(word)
print(len(vowels))

