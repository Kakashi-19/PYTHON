import pprint
print('Enter text to count the number of  each letter in the text')
text = input()
num = {}
for letter in text.upper():
    num.setdefault(letter, 0)
    num[letter] += 1

pprint.pprint(num) #to print it better

newtext = pprint.pformat(num)         # saves the pprint output as a string value for futher use

