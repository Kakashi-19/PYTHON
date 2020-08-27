
import webbrowser, sys, pyperclip

#https://www.google.co.in/search?safe=off&sxsrf=ALeKk03Lwy6-yTMaAHcG3qdGkkU5i8CAXQ:1588065767779&q=SEARCH

a = sys.argv
if len(a) > 1:
    search = ' '.join(a[1:])
    webbrowser.open('https://www.google.co.in/search?safe=off&sxsrf=ALeKk03Lwy6-yTMaAHcG3qdGkkU5i8CAXQ:1588065767779&q=' + search)
else:
    b = pyperclip.paste()
    webbrowser.open('https://www.google.co.in/search?safe=off&sxsrf=ALeKk03Lwy6-yTMaAHcG3qdGkkU5i8CAXQ:1588065767779&q=' + b)
    
