import requests, bs4

res = requests.get('http://portal.lnct.ac.in/Accsoft2/Parents/StuAttendanceStatus.aspx')
res.raise_for_status()
att = bs4.BeautifulSoup(res.text, 'html.parser')
attend = att.select('#ctl00_ContentPlaceHolder1_UpdatePanel1 > table > tbody > tr:nth-child(2)')
print(attend)