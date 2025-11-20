'''
css selector    :   To locate the elements using any attribute, we go for css selector
                    SYNTAX  :   tagname[attr_name="attr_value"]


'''


# import time
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
# driver.find_element('css selector', 'input[id="user-name"]').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('css selector', 'input[placeholder="Password"]').send_keys('secret_sauce')
# time.sleep(1)
# driver.find_element('css selector', 'input[type="submit"]').click()

####################################################################################


# import time
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.facebook.com/r.php')
# time.sleep(3)
#
# driver.find_element('css selector','input[name="firstname"]').send_keys('jiyu')
# time.sleep(3)
#
# driver.find_element('css selector','input[name="lastname"]').send_keys('abbot')
# time.sleep(3)
#
# driver.find_element('css selector', 'input[name="reg_email__"]').send_keys('jiyu@gmail.com')
# time.sleep(3)
#
# driver.find_element('css selector', 'input[name="reg_passwd__"]').send_keys('art@12345')
# time.sleep(3)


#######################################################################################################


# import time
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
#
# driver.find_element('css selector', 'a[class="ico-register"]').click()
# time.sleep(2)
# driver.find_element('css selector', 'input[id="gender-male"]').click()
# time.sleep(2)
# driver.find_element('css selector', 'input[id="FirstName"]').send_keys('artlover')
# time.sleep(2)
# driver.find_element('css selector', 'input[id="LastName"]').send_keys('creativity')
# time.sleep(2)
# driver.find_element('css selector', 'input[id="Email"]').send_keys('art@gmail.com')
# time.sleep(2)
# driver.find_element('css selector', 'input[id="Password"]').send_keys('8812345')
# time.sleep(2)
# driver.find_element('css selector', 'input[id="ConfirmPassword"]').send_keys('8812345')
# time.sleep(2)
#
# driver.close()
