from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")

driver.get("http://www.testyou.in/Login.aspx")
driver.maximize_window()

path = "C:\selenium_projects\data\DemoCredntial_DataDrivenTesting.xlsx"

driver.find_element_by_xpath('//*[@id="ctl00_CPHContainer_txtUserLogin"]').send_keys('fmahmud836')
driver.find_element_by_xpath('//*[@id="ctl00_CPHContainer_txtPassword"]').send_keys('@Tamim2000')
driver.find_element_by_xpath('//*[@id="ctl00_CPHContainer_btnLoginn"]').click()

t = driver.title
print(t)