from selenium import webdriver
f = open('.password', 'r')
readPassword = f.read()

browser = webdriver.Chrome()
isNotSuccessful = False

def SwitchTo(input):
    SwitchTo = browser.find_element_by_id(input)
    SwitchTo.click()
    try:
        Error =  browser.find_element_by_id('pageContent_ClassScheduleUC_ErrorMessageTable')
    except NoSuchElementException:
        return False
    else:
        return True

while 1 and isNotSuccessful:
    browser.get('https://my.sa.ucsb.edu/gold/login.aspx')
    NetId = browser.find_element_by_id('pageContent_userNameText')
    password = browser.find_element_by_id('pageContent_passwordText')
    login = browser.find_element_by_id('pageContent_loginButton')
    NetId.send_keys('yanxi')
    password.send_keys(readPassword)
    login.click()
    MyClassSchedule = browser.find_element_by_xpath("//*[@id='ctl05']")
    MyClassSchedule.click()
    Switch154 = browser.find_element_by_id('pageContent_CourseList_SwitchCourseButton_1')
    Switch154.click()
    isNotSuccessful = SwitchTo('pageContent_ClassScheduleUC_dl_coursegroup_PrimarySections_0_SecondarySections_0_SwitchLinkSecondary_2') or SwitchTo('pageContent_ClassScheduleUC_dl_coursegroup_PrimarySections_0_SecondarySections_0_SwitchLinkSecondaryAlt_3')
    logout = browser.find_element_by_xpath("//*[@id='headerTable']/tbody/tr[2]/td[2]/a")
    logout.click()
