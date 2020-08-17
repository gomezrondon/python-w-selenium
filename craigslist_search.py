from selenium import webdriver

driver = webdriver.Chrome("C:\\Program Files\\Selenium\\chromedriver.exe")
driver.get('https://cariboo.craigslist.org/')


driver.find_element_by_xpath("//*[@id='sss0']/li[23]/a/span").click()
#hacemos loop con find_element"s" tiene una s al final
elements = driver.find_elements_by_class_name("hdrlnk")
for post in elements:
    print(post.text)
