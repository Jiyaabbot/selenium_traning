# '''
# link text   :   The text present between the anchor tag, we call it as a link text.
#                 To locate the link text, we go for "link text" locator
#
# '''
#
# import time
#
# from selenium import webdriver
#
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver = webdriver.Chrome(opts)
#
#
# driver.get("https://demowebshop.tricentis.com/")
# time.sleep(3)
#
# driver.find_element("link text",'Register').click()
# time.sleep(2)
#
# driver.find_element("link text",'Shopping cart').click()
# time.sleep(2)
#
# driver.close()

###########################################################################################333

# import time
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# driver.find_element("link text",'Women').click()
# time.sleep(2)
#
# driver.find_element("link text",'Men').click()
# time.sleep(2)
#
# driver.find_element("link text",'Genz').click()
# time.sleep(2)







