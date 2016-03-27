from selenium import webdriver
f = open('.password', 'r')
readPassword = f.read()
count = 5
is154NotSuccessful = True
is165NotSuccessful = True
is138NotSuccessful = True

def SwitchTo(input):
    SwitchTo = browser.find_element_by_id(input)
    SwitchTo.click()
    try:
        Error =  browser.find_element_by_id('pageContent_ClassScheduleUC_ErrorMessageTable')
    except NoSuchElementException:
        return False
    else:
        return True

browser = webdriver.Chrome()
while 1 and (is154NotSuccessful or is165NotSuccessful or is138NotSuccessful):
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
    MyClassSchedule = browser.find_element_by_xpath("//*[@id='ctl05']")
    MyClassSchedule.click()
    if is154NotSuccessful:
        Switch154 = browser.find_element_by_id('pageContent_CourseList_SwitchCourseButton_1')
        Switch154.click()
        is154NotSuccessful = SwitchTo('pageContent_ClassScheduleUC_dl_coursegroup_PrimarySections_0_SecondarySections_0_SwitchLinkSecondary_2') and SwitchTo('pageContent_ClassScheduleUC_dl_coursegroup_PrimarySections_0_SecondarySections_0_SwitchLinkSecondaryAlt_3')

    if is165NotSuccessful:
        MyClassSchedule = browser.find_element_by_xpath("//*[@id='ctl05']")
        MyClassSchedule.click()
        Switch165 = browser.find_element_by_id('pageContent_CourseList_SwitchCourseButton_2')
        Switch165.click()
        is165NotSuccessful = SwitchTo('pageContent_ClassScheduleUC_dl_coursegroup_PrimarySections_0_SecondarySections_0_SwitchLinkSecondaryAlt_1')

    if is138NotSuccessful:
        MyClassSchedule = browser.find_element_by_xpath("//*[@id='ctl05']")
        MyClassSchedule.click()
        Switch138 = browser.find_element_by_id('pageContent_CourseList_SwitchCourseButton_0')
        Switch138.click()
        is138NotSuccessful = SwitchTo('pageContent_ClassScheduleUC_dl_coursegroup_PrimarySections_0_SecondarySections_0_SwitchLinkSecondaryAlt_1')

    logout = browser.find_element_by_xpath("//*[@id='headerTable']/tbody/tr[2]/td[2]/a")
    logout.click()
    count -= 1
    if count == 0:
        browser.close()

