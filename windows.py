from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

o = webdriver.ChromeOptions()
o.add_argument("disable-extensions")
o.add_argument("--start-maximized")
o.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"  ## This line define path of browser. In this case, Google Chrome
driver = webdriver.Chrome(executable_path=r"C:\drivers\chromedriver.exe", options=o)

# driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")

driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()

print(driver.current_window_handle)  # CDwindow-F97BA6F1D14A7B2819AE48106C891D5C #parent

handles = driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title == 'Frames & windows':
        driver.close()  # close the parent windows
