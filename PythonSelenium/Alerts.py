from selenium import webdriver

driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

driver.find_element_by_css_selector("#name").send_keys("option3")
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert()
print(alert.text)
alert.accept()     # to select Ok from Alert box
alert.dismiss()



