from select import select

from selenium import webdriver

#driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")

driver = webdriver.Firefox(executable_path="c:\\geckodriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")

#driver.find_element_by_name("name").send_keys("Monika")
#driver.find_element_by_css_selector("input[name='name']").send_keys("Monika")
#driver.find_element_by_name("email").send_keys("Bhoraniya")
#driver.find_element_by_id("examplecheck1").click()


#dropdown = select(driver.find_element_by_id("exampleFormControlSelect1"))
#dropdown.select_by_visible_text("female")
#dropdown.select_by_index(0)
#dropdown.select_by_value()
  # create object


#select class provide the methods

#dropdown = select(driver.find_element_by_id("exampleFormControlSelect1"))

#dropdown.select_by_visible_text("female")






#driver.find_element_by_xpath("//input[@type='submit']").click()

message = (driver.find_element_by_class_name("alert-success").text)
assert "success" in message

#//*[contains(@class,'alert-success')]
#[class*='alert-success']







