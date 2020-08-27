#program to count number of vowels and consonants in a string
#! python3
print('Enter a Word or Sentence')
word = input()
newWord = word.lower()
letter = {}
for i in newWord:
    letter.setdefault(i, 0)
    letter[i] += 1
letter.setdefault('a', 0)
letter.setdefault('e', 0)
letter.setdefault('i', 0)
letter.setdefault('o', 0)
letter.setdefault('u', 0)
noVowels = letter['a'] + letter['e'] + letter['i'] + letter['o'] + letter['u']
letter.setdefault('.', 0)
noConsonants = len(list(''.join(newWord.split()))) - noVowels - letter['.']
print("\nThere are " + str(noVowels) + " Vowels and " + str(noConsonants) + ' Consonants in : ' + word )
