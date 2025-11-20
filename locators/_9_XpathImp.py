'''
Dependent-Independent xpath
    *   Identify the dependent and independent elements
    *   Write the xpath of the independent element
    *   Traverse back until we get the common match for dependent-independent element
    *   Continue the xpath for the dependent element


'''

#Eg1. wap to click on the checkbox of Ruby in demo.html

import time

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Jiya Abbot\PycharmProjects\selenium_traning\demo.html')
# time.sleep(2)
#
# driver.find_element("xpath",'//td[text()="Ruby"]/..//input[@name="download"]').click()
#
# driver.close()

############################################################################################################

#Eg2.    wap to click on the download link of windows in demo.html


# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Jiya Abbot\PycharmProjects\selenium_traning\demo.html')
# time.sleep(2)
#
# driver.find_element('xpath', '//td[text()="Windows"]/..//a[text()="Download"]').click()

################################################################################################################

#Eg3.    wap to click on the release notes of python 3.13.4 in https://www.python.org/


# from selenium import webdriver
#
# driver = webdriver.Firefox()
#
# driver.get('https://www.python.org/')
# time.sleep(2)
#
# driver.find_element('xpath', '(//a[text()="Downloads"])[1]').click()
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Python 3.13.4"]/../..//a[text()="Release Notes"]').click()
#

###############################################################################################################

#Eg4.    wap to print the sellprice and buyprice of bitcoin in https://www.iforex.in/tools/live-rates

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.iforex.in/tools/live-rates')
# time.sleep(3)
#
# gold_sellprice = driver.find_element("xpath",'(//div[text()="Gold"]/../..//span)[2]')
# print(f'The sell price of gold is {gold_sellprice.text}')
#
# gold_buyprice = driver.find_element("xpath",'(//div[text()="Gold"]/../..//span)[3]')
# print(f'The buy price of gold is {gold_buyprice.text}')

######################################################################################################################

#Eg5. Wap to print the price of mrf in https://in.tradingview.com

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://in.tradingview.com/')
# time.sleep(2)
#
# driver.find_element("xpath",'//span[text()="Search"]').click()
# time.sleep(2)
#
# driver.find_element("xpath",'//input[@name="query"]').send_keys('mrf')
# time.sleep(2)
#
# driver.find_element("xpath",'(//span[@class="icon-KLRTYDjH"])[1]').click()
# time.sleep(2)
#
# mrf_price = driver.find_element("xpath",'//span[text()="MRF"]/../../..//span[@class="priceWrapper-qWcO4bp9"]')
# print(mrf_price.text)




















