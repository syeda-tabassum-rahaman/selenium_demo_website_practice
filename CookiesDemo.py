from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")

driver.get("https://www.amazon.in/")

#capture all the cookies created by browser

cookies = driver.get_cookies()
print(len(cookies))    #print number of cookies have been created
print(cookies)        #print all the cookies pairs

#adding new cookie to the browser

cookie = {"name": "Mycookie", "value": "1234567"}
driver.add_cookie(cookie)
cookies = driver.get_cookies()
print(len(cookies))   #print number of cookies have been created
print(cookies)        #print all the cookies pairs


#deleting cookie
driver.delete_cookie("Mycookie")
cookies = driver.get_cookies()
print(len(cookies))   #print number of cookies have been found
print(cookies)        #print all the cookies pairs after deleting the cookies

#deleting all the cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()
print(len(cookies))