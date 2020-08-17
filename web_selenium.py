from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("C:\\Program Files\\Selenium\\chromedriver.exe")
browser.get('http://seleniumhq.org/')

# elem = browser.find_element_by_link_text('Downloads')
#
# print(elem.text)
# print(elem.get_attribute('href'))
# elem.click()

#----
search_bar = browser.find_element_by_id('gsc-i-id1')
search_bar.send_keys('Downloads')
search_bar.send_keys(Keys.ENTER)
# browser.close()

