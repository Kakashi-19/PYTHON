import requests, bs4
lol = input()
def price(url):
    res = requests.get(url)
    res.raise_for_status()
    att = bs4.BeautifulSoup(res.text, 'html.parser')
    attend = att.select('')
    return attend[0].text.strip()

data = price(lol)
print(data)