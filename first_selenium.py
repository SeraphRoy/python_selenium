from selenium import webdriver
f = open('.password', 'r')

browser = webdriver.Chrome()
browser.get('https://my.sa.ucsb.edu/gold/login.aspx')
NetId = browser.find_element_by_id('pageContent_userNameText')
password = browser.find_element_by_id('pageContent_passwordText')
login = browser.find_element_by_id('pageContent_loginButton')
NetId.send_keys('yanxi')
readPassword = f.read()
password.send_keys(readPassword)
login.click()
