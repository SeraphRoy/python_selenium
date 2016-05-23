from selenium import webdriver
import smtplib
f = open('.password', 'r')
emailPW = open('.email', 'r')
readPassword = f.read()
emailPassword = emailPW.read()
smtpAccount = "royxagain@gmail.com"
sender = "royxagain@gmail.com"
receiver = "royxagain@gmail.com"
count = 5
spaceLimit = 10

browser = webdriver.Chrome()
while 1:
    if count == 0:
        browser = webdriver.Chrome()
        count = 5
    browser.get('https://my.sa.ucsb.edu/gold/login.aspx')
    NetId = browser.find_element_by_id('pageContent_userNameText')
    password = browser.find_element_by_id('pageContent_passwordText')
    login = browser.find_element_by_id('pageContent_loginButton')
    NetId.send_keys('yanxi')
    password.send_keys(readPassword)
    login.click()
    FindCourse = browser.find_element_by_xpath("//*[@id='ctl07']")
    FindCourse.click()
    browser.find_element_by_xpath("//*[@id='pageContent_quarterDropDown']/option[1]").click()
    browser.find_element_by_xpath("//*[@id='pageContent_subjectAreaDropDown']/option[18]").click()
    browser.find_element_by_id('pageContent_searchButton').click()
    CS160Space = browser.find_element_by_xpath("//*[@id='pageContent_CourseList_PrimarySections_11']/tbody/tr/td/table/tbody/tr[1]/td[7]").text
    space = "CS160Space"
    if int(CS160Space) < spaceLimit:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        #server.ehlo()
        server.login(smtpAccount, emailPassword)
        msg = "\nHello! " + space + " is less than" + str(spaceLimit)# The /n separates the message from the headers (which we ignore for this example)
        server.sendmail(sender,receiver, msg)
        browser.close()
        break

    logout = browser.find_element_by_xpath("//*[@id='headerTable']/tbody/tr[2]/td[2]/a")
    logout.click()
    count -= 1
    if count == 0:
        browser.close()

