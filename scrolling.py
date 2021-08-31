from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

driver.maximize_window()
#scroll down by pixel
#driver.execute_script("window.scrollBy(0,1000)","")

#scroll down page till the element is visible
#flag = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/table[1]/tbody/tr[69]/td[2]")
#driver.execute_script("arguments[0].scrollIntoView();",flag)

#scroll down till the end

driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")