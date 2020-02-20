import time
import schedule
from selenium import  webdriver
from selenium.webdriver.common.keys import Keys

while True:
    driver =  webdriver.Chrome("C:\\cdriver.exe")
    driver.get("https://www.gmail.com/")
    time.sleep(1)
    driver.find_element_by_name("identifier").send_keys("gokulprasanth")
    driver.find_element_by_id("identifierNext").send_keys(Keys.ENTER)
    time.sleep(2)
    driver.find_element_by_name("password").send_keys("9876543210")
    driver.find_element_by_id("passwordNext").send_keys(Keys.ENTER)
    time.sleep(2)
    driver.close()
"""schedule.every(15).seconds.do(test)
while 1:
	schedule.run_pending()
	time.sleep(0)"""