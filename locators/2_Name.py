'''import time

from selenium import webdriver

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver = webdriver.Chrome(opts)
time.sleep(2)

driver.get('https://www.instagram.com/')
time.sleep(2)

driver.find_element('name','username').send_keys('chetnarani')
time.sleep(1)

driver.find_element('name','password').send_keys('chetna9821')
time.sleep(1) '''


