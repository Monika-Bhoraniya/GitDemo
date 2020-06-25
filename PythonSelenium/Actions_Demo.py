import action as action
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
#driver.get("https://www.familysearch.org/en/")

Action = ActionChains(driver)
#action.move_to_element(driver.find_element_by_id("search")).perform()
#action.move_to_element(driver.find_element_by_link_text("Genealogies")).click().perform()

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action.double_click(driver.find_element_by_id("double-click")).perform()

alert = driver.switch_to.alert()
assert "You double clicked me!!!, You got to be kidding me" == alert.text
alert.accept()
