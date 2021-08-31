from selenium import webdriver
from selenium.webdriver.chrome.options import  Options

chromeOptions = Options()
chromeOptions.add_experimental_option('prefs', {'download.default_directory': 'C:\selenium_projects\source'})


driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe", chrome_options=chromeOptions)

driver.get("http://demo.automationtesting.in/FileDownload.html")

driver.maximize_window()

driver.find_element_by_id('textbox').send_keys('HI, my name is chowa kowa mowa! :)')
driver.find_element_by_id('createTxt').click()
driver.find_element_by_id('link-to-download').click()