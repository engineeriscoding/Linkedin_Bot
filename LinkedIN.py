from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
driver = r"C:\Users\Admin\Downloads\chromedriver_win32\chromedriver"
browser = webdriver.Chrome(driver)
browser.get("https://www.linkedin.com/uas/login")
file = open(r"C:\Users\Admin\Desktop\config.txt")
lines = file.readlines()
emailid = lines[0]
password = lines[1]
browser.find_element_by_id("username").send_keys(emailid)
browser.find_element_by_id("password").send_keys(password)
browser.find_element_by_xpath("//button [@type = 'submit']").click()

names = ["Engr. Rahib Bin Basheer","Syed Minhaj","Mossad Mahmoud Eltohami"]
count = 0
for name in names:
    browser.find_element_by_xpath("//input [@type = 'text']").send_keys(name)
    sleep(5)
    browser.find_element_by_xpath("//input[@type = 'text']").send_keys(Keys.ENTER)
    sleep(5)
    browser.find_element_by_xpath("//button[text()= 'Message']").click()
    sleep(3)
    message = " hello , im Abhishek. Hope you are doing well."
    sleep(4)
    if count == 0:
        browser.find_element_by_xpath("//div[@role = 'textbox']").send_keys(message)
    else:
        browser.find_elements_by_xpath("//div[@role = 'textbox']")[count].send_keys(message)
    sleep(6)
    if count == 0:
        browser.find_element_by_xpath("//button [@type = 'submit']").click()
    else:
        browser.find_elements_by_xpath("//button [@type = 'submit']")[count].click()
    count = count+1
    sleep(5)
    browser.find_element_by_xpath("//input [@type = 'text']").clear()




