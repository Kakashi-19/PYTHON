'''A Palindrome is a word that spells the same from both sides,
  example is Hannah '''
print('Enter a Word to check if its a Palindrome')
word = list(input().lower())
def rev(l):
    l.reverse()
    return l
if word == rev(word):
    print('Given Word is a Palindrome')
else:
    print('Given word is not a Palindrome')


