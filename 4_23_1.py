from selenium import webdriver
import time
import requests
from selenium.webdriver.chrome.options import Options
import json
from bs4 import BeautifulSoup
#chrome_options = Options()
# chrome_options.add_argument("--headless")
# driver = webdriver.Chrome(executable_path="text\chromedriver.exe",
#                          options=chrome_options)
driver = webdriver.Chrome()
driver.get('https://sschool.tp.edu.tw/Login.action?schNo=403302')
# element = driver.find_element_by_class_name("gLFyf.gsfi")
# element.send_keys("Selenium Python")
button1 = driver.find_element_by_class_name("login-key")
button1.click()
element1 = driver.find_element_by_id("username")
element1.send_keys("lssh10831037")
element2 = driver.find_element_by_id("password")
element2.send_keys("0215jeff")
button2 = driver.find_element_by_id("btnLogin")
button2.click()
time.sleep(4)
button3 = driver.find_elements_by_xpath(
    "/html/body/div[1]/section/div/div/div/div/div[3]/div/div/div[1]/button")
button3[-1].click()
time.sleep(2)
button6 = driver.find_elements_by_xpath(
    "/html/body/div[1]/nav/div[1]/div/ul/li[2]/a")
button6[-1].click()
time.sleep(2)
button7 = driver.find_elements_by_xpath(
    "/html/body/div[1]/nav/div[1]/div/ul/li[2]/div/div/li[1]/a")
button7[-1].click()
time.sleep(2)
button4 = driver.find_elements_by_xpath(
    "/html/body/div[1]/section/div/div/div/table/tbody/tr/td[1]/div[1]/div[3]/div[3]/div/table/tbody/tr[5]")
button4[-1].click()
time.sleep(2)
button8 = driver.find_elements_by_xpath(
    "/html/body/div[1]/section/div/div/div/table/tbody/tr/td[2]/div/div[1]/table/tbody/tr[1]/td[1]/div/div[3]/div[3]/div/table/tbody/tr[3]")
button8[-1].click()
time.sleep(2)
dicts = {}
for a in range(2, 8):
    subject = driver.find_element_by_xpath(
        "/html/body/div[1]/section/div/div/div/table/tbody/tr/td[2]/div/div[1]/table/tbody/tr[2]/td/div/div[3]/div[3]/div/table/tbody/tr[{}]/td[5]".format(a))
    grade = driver.find_element_by_xpath(
        "/html/body/div[1]/section/div/div/div/table/tbody/tr/td[2]/div/div[1]/table/tbody/tr[2]/td/div/div[3]/div[3]/div/table/tbody/tr[{}]/td[6]".format(a))
    dicts[subject.get_attribute("title")] = grade.get_attribute("title")
file = '4_23_3.json'
with open(file, 'w', encoding='utf-8') as obj:
    json.dump(dicts, obj, ensure_ascii=False, sort_keys=True, indent=2)
print("Done")
