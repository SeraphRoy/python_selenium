from selenium import webdriver
f = open('.password', 'r')
readPassword = f.read()

browser = webdriver.Chrome()
isSelected = False
while 1:
    browser.get('https://my.sa.ucsb.edu/gold/login.aspx')
    NetId = browser.find_element_by_id('pageContent_userNameText')
    password = browser.find_element_by_id('pageContent_passwordText')
    login = browser.find_element_by_id('pageContent_loginButton')
    NetId.send_keys('yanxi')
    password.send_keys(readPassword)
    login.click()
    FindCourses = browser.find_element_by_id('ctl07')
    FindCourses.click()
    quarter = browser.find_element_by_xpath("//*[@id='pageContent_quarterDropDown']/option[1]")
    quarter.click()
    subject = browser.find_element_by_xpath("//*[@id='pageContent_subjectAreaDropDown']/option[18]")
    subject.click()
    beginSearch = browser.find_element_by_id('pageContent_searchButton')
    beginSearch.click()
    CS177Section1 = browser.find_element_by_id('pageContent_CourseList_PrimarySections_15_SecondarySections_0_AddLinkSecondary_0')
    if CS177Section1.get_attribute("class") != "aspNetDisabled":
        CS177Section1.click()
        isSelected = True
    logout = browser.find_element_by_xpath("//*[@id='headerTable']/tbody/tr[2]/td[2]/a")
    logout.click()
