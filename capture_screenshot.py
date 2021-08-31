from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")

driver.get("https://www.amazon.in/")
driver.maximize_window()

#driver.save_screenshot("C:\selenium_projects\data\login.png")

driver.get_screenshot_as_file("C:\selenium_projects\data\login2.jpg")
