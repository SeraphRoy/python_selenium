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
spaceLimit160 = 10
spaceLimit176A = 10
spaceLimit20 = 5
spaceLimitW12 = 10

def sendEmail(message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    #server.ehlo()
    server.login(smtpAccount, emailPassword)
    server.sendmail(sender,receiver, message)


browser = webdriver.Chrome()
while 1:
    try:
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
        beginSearch = browser.find_element_by_id('pageContent_searchButton')
        beginSearch.click()
        CS160Space = browser.find_element_by_xpath("//*[@id='pageContent_CourseList_PrimarySections_11']/tbody/tr/td/table/tbody/tr[1]/td[7]").text
        space160 = "CS160Space"
        CS176ASpace = browser.find_element_by_xpath("//*[@id='pageContent_CourseList_PrimarySections_13']/tbody/tr/td/table/tbody/tr[1]/td[7]").text
        space176A = "CS176ASpace"
        FindCourse = browser.find_element_by_xpath("//*[@id='ctl07']")
        FindCourse.click()
        browser.find_element_by_xpath("//*[@id='pageContent_subjectAreaDropDown']/option[23]").click()
        beginSearch = browser.find_element_by_id('pageContent_searchButton')
        beginSearch.click()
        Earth20Space = browser.find_element_by_xpath("//*[@id='pageContent_CourseList_PrimarySections_7_SecondarySections_0']/tbody/tr[1]/td/table/tbody/tr[1]/td[8]").text
        space20 = "Earch20Space"
        FindCourse = browser.find_element_by_xpath("//*[@id='ctl07']")
        FindCourse.click()
        browser.find_element_by_xpath("//*[@id='pageContent_subjectAreaDropDown']/option[40]").click()
        beginSearch = browser.find_element_by_id('pageContent_searchButton')
        beginSearch.click()
        GeogW12Space = browser.find_element_by_xpath("//*[@id='pageContent_CourseList_PrimarySections_3']/tbody/tr/td/table/tbody/tr[1]/td[7]").text
        spaceW12 = "GeogW12Space"
        if int(CS160Space) < spaceLimit160:
            msg = "\nHello! " + space160 + " is less than" + str(spaceLimit160)# The /n separates the message from the headers (which we ignore for this example)
            sendEmail(msg)
            browser.close()
            break

        if int(CS176ASpace) < spaceLimit176A:
            msg = "\nHello! " + space176A + " is less than" + str(spaceLimit176A)# The /n separates the message from the headers (which we ignore for this example)
            sendEmail(msg)
            browser.close()
            break

        if int(Earth20Space) < spaceLimit20:
            msg = "\nHello! " + space20 + " is less than" + str(spaceLimit20)# The /n separates the message from the headers (which we ignore for this example)
            sendEmail(msg)
            browser.close()
            break

        if int(GeogW12Space) < spaceLimitW12:
            msg = "\nHello! " + spaceW12 + " is less than" + str(spaceLimitW12)# The /n separates the message from the headers (which we ignore for this example)
            sendEmail(msg)
            browser.close()
            break

        logout = browser.find_element_by_xpath("//*[@id='headerTable']/tbody/tr[2]/td[2]/a")
        logout.click()
    except Exception as e:
        print e
        browser.close()
        browser = webdriver.Chrome()
    count -= 1
    if count == 0:
        browser.close()
