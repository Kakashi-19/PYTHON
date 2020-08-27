#! python3
import re, pyperclip
#TODO: PHONE NUMBER EXTRACTOR
phRegex = re.compile(r'''
( ((\d\d\d) | (\(\d\d\d\)))?                           #area code 
 (\s|-)             #seperator
 \d\d\d                 #first 3 digits
 -                         #seperator
 (\d\d\d\d)                #last 4 digits
 ((ext(\.)?\s|x)
 (\d{2,5}))?   )           #extensions 
                           ''', re.VERBOSE)


#EMAIL EXTRACTOR
emRegex = re.compile('''
[a-zA-Z0-9_+.]+ #username
@
[a-zA-Z0-9_+.]+ #domainname

''', re.VERBOSE)
text = pyperclip.paste()
email = emRegex.findall(text)
phone = phRegex.findall(text)
numbers = []
for i in phone:
    numbers.append(i[0])
n = '\n'.join(numbers)
e = '\n'.join(email)
extract = 'Phone List\n' + n + '\n' + 'Email List\n' + e
#TODO: ARRANGE AND ADD EXTRACTED FILES TO CLIPBOARD
pyperclip.copy(extract)
