import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
driver.get("https://www.makemytrip.com/")
driver.find_element_by_id("fromCity").click()
driver.find_element_by_css_selector("input*[placeholder='from']").send.keys("del")
time.sleep(2)
cities = driver.find_elements_by_css_selector("p[class*='blackText']")
print(len(cities))
for city in cities:
    if city.text =="Del Rio,United States":
        city.click()
    break

