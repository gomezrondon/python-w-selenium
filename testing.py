
from selenium import webdriver
import pathlib
import os
#https://duckduckgo.com/?q=google&atb=v140-3__&ia=web
#https://codebeautify.org/Xpath-Tester


# path = os.path.abspath('duckduck.html')
# url = pathlib.Path(path).as_uri()

driver = webdriver.Chrome("C:\\Program Files\\Selenium\\chromedriver.exe")
driver.get('https://duckduckgo.com/')
# browser.get(url)

#1) select the search bar
# //input[@id='search_form_input_homepage']  (search box)
# //input[@id='search_button_homepage'] (botton lupa)
# search_bar = driver.find_element_by_xpath('//input[@id="search_form_input_homepage"]')
search_bar = driver.find_element_by_name('q')

#2) set the term to be search
search_bar.send_keys('vodka')
#3) click the search button
# driver.find_element_by_xpath('//input[@id="search_button_homepage"]').click()
search_bar.submit()

#4) get al the results (10 in this case)
results = driver.find_elements_by_xpath("//*[starts-with(@id,'r1-')]")
#5) print the numbre of links
print(len(results))

#6) print each link with its resume
for result in results:
    print(result.get_attribute("href"))
    print(result.text)



# driver.close()


