'''import time

from selenium import webdriver

opts= webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)

driver = webdriver.Chrome(opts)

## launch the application
driver.get('https://www.flipkart.com/')
time.sleep(3)

## maximize browser
driver.maximize_window()
time.sleep(3)

## minimize window
driver.minimize_window()
time.sleep(3)

## to get back
driver.back()
time.sleep(3)

## to go forword
driver.forward()
time.sleep(3)

## to refresh
driver.refresh()
time.sleep(3)

## fullscreen window
driver.fullscreen_window()
time.sleep(3)

## properties
print(driver.current_url)
print(driver.title)
print(driver.name)

##################################################################################################3

## by default the screenshot will be saved in the same location as our python file.

## take screenshot
driver.save_screenshot("flipkart.ss.png")

## to save the screenshot in a different location
driver.save_screenshot(r'C:\Users\Jiya Abbot\PycharmProjects\Screenshot\flipkar.ss.png')

## close the browser
driver.close() '''
