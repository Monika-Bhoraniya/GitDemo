

from selenium import webdriver

#driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="c:\\geckodriver.exe")
driver = webdriver.Ie(executable_path="c:\\IEDriverServer.exe")
#driver.maximize_window()
driver.get("https://rahulshettyacademy.com/#/index")     #get method will help to hit on  page URL

print(driver.title)     #page title
print(driver.current_url)

#driver.get("https://rahulshettyacademy.com/#/practice-project")
#driver.back()
#driver.refresh()

#driver.close() #only current windows get close.
#driver.quit() #all windows get closed.(multiple tab)
