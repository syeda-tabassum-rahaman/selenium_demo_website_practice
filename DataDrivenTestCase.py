import XLUtils
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")

driver.get("http://www.testyou.in/Login.aspx")
driver.maximize_window()

path = "C:\selenium_projects\data\DemoCredntial_DataDrivenTesting.xlsx"

rows = XLUtils.getRowCount(path, 'Sheet1')

for r in range(2, rows+1):
    username = XLUtils.readData(path, "Sheet1", r, 1)
    password = XLUtils.readData(path,"Sheet1", r, 2)
    driver.find_element_by_xpath('//*[@id="ctl00_CPHContainer_txtUserLogin"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="ctl00_CPHContainer_txtPassword"]').send_keys(password)

    driver.find_element_by_xpath('//*[@id="ctl00_CPHContainer_btnLoginn"]').click()

    if driver.title =="Student Dashboard | Test Maker - TestYou":
        print("Test is passed")
        XLUtils.writeData(path, "Sheet1", r, 3, "Test Passed")
        driver.find_element_by_xpath('//*[@id="ctl00_headerTopStudent_lnkbtnSignout"]').click()
    else:
        print("test failed")
        XLUtils.writeData(path, "Sheet1", r, 3, "test failed")
        driver.get("http://www.testyou.in/Login.aspx")






