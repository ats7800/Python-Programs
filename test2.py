# Simple assignment
from selenium.webdriver import Chrome
import time

driver = Chrome()

driver.get('https://www.instagram.com/')
time.sleep(6)
# driver.find_elements_by_class_name("zyHYP")[0].click()
driver.find_elements_by_class_name("zyHYP")[0].send_keys("rewritingthestars_ashu")
driver.find_elements_by_class_name("zyHYP")[1].send_keys("atsking#1R")
driver.find_elements_by_tag_name("button")[0].click()
driver.find_elements_by_tag_name("button")[1].click()
print('done')



