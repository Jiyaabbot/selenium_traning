'''
text    :   It is a property of a web-element.
            It will give the text of the web-element
            SYNTAX  :   web_element.text

'''

import time
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# ele = driver.find_element('xpath', '//a[@data-group="home"]')
# print(ele.text)

#############################################################################################################



# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.python.org/')
# time.sleep(2)
#
# element = driver.find_element("xpath",'//div[@class="main-footer-links"]')
#
# print(element.text)

####################################################################################################################

#
# '''
# get_attribute   :   This is an attribute of a web-element.
#                     It will give the attribute values.
#
#                     SYNTAX  :   web_element.get_attribute("attr_name")
# '''



# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# home = driver.find_element('xpath', '(//a[text()="Home"])[1]')
# print(home.get_attribute('href'))
# print(home.get_attribute('style'))
# print(home.get_attribute('class'))
# print(home.get_attribute('data-group'))

#####################################################################################################

######################### reading tables ####################################

# import time
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# table_data = driver.find_elements('xpath', '//table[@name="BookTable"]//td')
# # print(table_data)       ## list of web-elements         ## [wb1, wb2, wb3, wb4,..]
#
# for r in range(2, 8):
#     for c in range(1, 5):
#         data = driver.find_element('xpath', f'//table[@name="BookTable"]//tr[{r}]/td[{c}]')
#         print(data.text, end='\t\t')
#     print()
