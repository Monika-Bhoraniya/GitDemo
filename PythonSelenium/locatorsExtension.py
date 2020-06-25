from selenium import webdriver
driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")

driver.get("https://login.salesforce.com/")
driver.find_elements_by_css_selector("#username").send_keys("Monika")
driver.find_elements_by_css_selector(".password").send_keys("Bhoraniya")
driver.find_elements_by_css_selector(".password").clear()
driver.find_element_by_link_text("Forgot Your Password?").click()
driver.find_element_by_xpath("//a[text()='cancel']").click()
print(driver.find_element_by_xpath("/form[@name='login']/div[1]/label"))
print(driver.find_elements_by_css_selector("form[name='login']label:nth-child(3)")
      .text)



