from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import json
import time

with open("config.json") as json_data:
    data = json.load(json_data)

user = data['github']['user']
print(user)
# print(data['github']['passwd'])

browser = webdriver.Chrome("C:\\Program Files\\Selenium\\chromedriver.exe")
browser.get('https://github.com/login?return_to=%2F'+user+'%3Ftab%3Drepositories')

user_input = browser.find_element_by_id('login_field')
user_input.send_keys(data['github']['user'])
time.sleep(1)
user_input = browser.find_element_by_id('password')
user_input.send_keys(data['github']['passwd'])
time.sleep(2)
user_input.send_keys(Keys.ENTER)

browser.get("https://github.com/new")

#id repository_name
repo_name = browser.find_element_by_id('repository_name')
response = pyautogui.prompt(text='Introduce Repo name:', title='Repository name')
repo_name.send_keys(response)
#id repository_description
repo_name = browser.find_element_by_id('repository_description')
response = pyautogui.prompt(text='Introduce Description', title='Repository Description')
repo_name.send_keys(response)

respuesta = pyautogui.confirm(text='', title='', buttons=['OK', 'Cancel'])

#does not work
if repo_name == 'OK':
    print('>>>>>>>>>>>>>>>> ' + respuesta)
    elem = browser.find_element_by_css_selector('button.btn-primary')
    elem.click()
