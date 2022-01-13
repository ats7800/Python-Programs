from selenium import webdriver

chromedriver = "/Users/ashutoshsingh/Downloads/chromedriver"
driver = webdriver.Chrome(chromedriver)

driver.get('http://www.nationalrail.co.uk/') # replaces "ie.navigate"
driver.find_element_by_id('sltArr').find_elements_by_tag_name('option')[1].click() # Selects the "Arrive" option