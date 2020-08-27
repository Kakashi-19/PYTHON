import inflect
import re

# Input
N = int(input())
num = list(map(int, input().split()))

# to convert to textual form
n2w = inflect.engine()
text = list(map(n2w.number_to_words, num))

# program for counting vowels in a string
vowelRegex = re.compile(r'[aeiou]', re.I)
vowels = vowelRegex.findall(' '.join(text))
a = len(vowels)
for i in num:
	if i == 100:
		a -= 2

#find no of pairs in given input whose sum equals number of vowels
pairs = []
for j in range(len(num)):
	for k in range(len(num)):
		if num[j]+num[k] == a and j != k:
			pairs.append((num[j], num[k]))

#Output
print(n2w.number_to_words(len(set(pairs))//2))