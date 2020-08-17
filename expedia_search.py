from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\\Program Files\\Selenium\\chromedriver.exe")
driver.get('https://www.expedia.com/')



# OJO hay que usar doble commillas afuera y comillas simples adentro
# abre la ventana where are you going?
driver.find_element_by_xpath("//div[@class='uitk-typeahead']//button[@class='uitk-faux-input']").click()
driver.find_element_by_xpath('//input[@placeholder="Where are you going?"]').send_keys("panama")
driver.find_element_by_xpath('//input[@placeholder="Where are you going?"]').send_keys(Keys.ENTER)

# driver.find_element_by_id("location-field-destination-dialog-input").click()


