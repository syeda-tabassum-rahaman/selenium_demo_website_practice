from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")

driver.get("file:///C:/selenium_projects/table1.html")

rows = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr"))
columns = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr[1]/th"))

print(rows)
print(columns)

