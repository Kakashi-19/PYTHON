@py "C:\Users\vaibhav pratap singh\Desktop\python\a.py" %*
@py

from selenium import  webdriver
import  time

browser = webdriver.Edge()
browser.get('http://portal1.lnct.ac.in/Accsoft2/Login.aspx')

browser.find_element_by_css_selector('#ctl00_cph1_rdp').click()
time.sleep(1)
browser.find_element_by_css_selector('#ctl00_cph1_txtStuUser').send_keys('11156824879')
browser.find_element_by_css_selector('#ctl00_cph1_txtStuPsw').send_keys('kanhaiya_13')
browser.find_element_by_css_selector('#ctl00_cph1_btnStuLogin').click()
time.sleep(1)
browser.find_element_by_css_selector('#ctl00_liAcademics > a > span').click()

browser.find_element_by_css_selector('#ctl00_lnkAttendanceStatus').click()



