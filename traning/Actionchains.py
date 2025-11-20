# '''
# The operations which involve mouse(Right click, double click, moue hovering, drag and drop, scrolling)/keyboard,
# we call them as "low-level" operations.
# To perform low-level operations in selenium, we go for ActionChains
#
# '''

#fname.send_keys(Keys.CONTROL + 'a')         ## select the data
# fname.send_keys(Keys.CONTROL + 'c')         ## copy the data
#
# ac_obj.send_keys(Keys.TAB).perform()        ## switching the control to last name
# lname.send_keys(Keys.CONTROL + 'v')         ## paste the data

#
#
# from selenium.webdriver.common.action_chains import ActionChains
#
# from selenium.webdriver.common.keys import Keys
#
# ac_obj = ActionChains(driver)

# #########################################################################################################################
#
# ########################## mouse hovering operation #########################
#
# import time
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# from selenium.webdriver.common.action_chains import ActionChains
#
# from selenium.webdriver.common.keys import Keys
#
# opts.add_experimental_option("detach",True)
# driver =webdriver.Chrome(opts)

# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# driver.maximize_window()
#
# ac_obj = ActionChains(driver)
#
# women = driver.find_element("xpath",'//a[@data-group="women"][1]')
# ac_obj.move_to_element(women).perform()
# time.sleep(2)
#
# studio = driver.find_element("xpath",'//a[text()="Studio"][1]')
# ac_obj.move_to_element(studio).perform()
# time.sleep(2)
#
# driver.close()

# # ##################################################################################################################
# #
# # ##################################### Double click #########################################
# #
# import time
#
# from selenium import webdriver
#
# from selenium.webdriver.common.action_chains import ActionChains
#
# from selenium.webdriver.common.keys import Keys
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver = webdriver.Chrome(opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
#
# ac_obj = ActionChains(driver)
#
# ele1 = driver.find_element('xpath', '//button[text()="Copy Text"]')
# ac_obj.double_click(ele1).perform()

# ########################################################################################################################
#
# import time
#
# from selenium import webdriver
#
# from selenium.webdriver.common.action_chains import ActionChains
#
# from selenium.webdriver.common.keys import Keys
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver = webdriver.Chrome()
#
# driver.get('https://www.facebook.com/r.php?entry_point=login')
#
# ac_obj = ActionChains(driver)
#
# ele = driver.find_element('xpath', '//div[text()="Create a new account"]')
# time.sleep(2)
# ac_obj.double_click(ele).perform()

# #################################################################################################################
#            ################################ Right click #########################################
#
# import time
#
# from selenium import webdriver
#
# from selenium.webdriver.common.action_chains import ActionChains
#
# from  selenium.webdriver.common.keys import Keys
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver = webdriver.Chrome()
#
# driver.get('https://www.facebook.com/r.php?entry_point=login')
# time.sleep(4)
#
# ac_obj = ActionChains(driver)
#
# ## To right_click on a specific element
# ele = driver.find_element('xpath', '//div[text()="Create a new account"]')
# time.sleep(3)
# ac_obj.context_click(ele).perform()

# ## ac_obj.context_click().perform()        ## It will right_click at the start of the application
#
# #
# # ################################################################################################################################
# #      #################################### Scrolling operations ###################################################
#
# import time
#
# from selenium import webdriver
#
# from selenium.webdriver.common.action_chains import ActionChains
#
# from selenium.webdriver.common.keys import Keys
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver = webdriver.Chrome()
#
#
# driver.get('https://www.swarovski.com/')
# time.sleep(2)
#
# ac_obj = ActionChains(driver)
#
# # ## page-down operation
# ac_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
#
# ### PAGE UP
# ac_obj.send_keys(Keys.PAGE_UP).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.PAGE_UP).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.PAGE_UP).perform()
# time.sleep(2)
#
# ## Scroll down to the end of the application
# ac_obj.send_keys(Keys.END).perform()
# time.sleep(3)
# ac_obj.send_keys(Keys.HOME).perform()
#

# #######################################################################################################################
#   ################################## to scroll to a particular web-element ############################
#
# import time
#
# from selenium import webdriver
#
# from selenium.webdriver.common.action_chains import ActionChains
#
# from selenium.webdriver.common.keys import Keys
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver = webdriver.Chrome()
#
# driver.get('https://www.swarovski.com/')
# time.sleep(2)
#
# ele = driver.find_element('xpath', '//h3[text()="Maximum brilliance"]')
# ac_obj = ActionChains()
#ac_obj.scroll_to_element(ele).perform()

# ################################################################################################################
#   ####################### Drag and drop ########################################
#
# import time
#
# from selenium import webdriver
#
# from selenium.webdriver.common.action_chains import ActionChains
#
# from selenium.webdriver.common.keys import Keys
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver = webdriver.Chrome()
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
# ac_obj = ActionChains(driver)
#
# ac_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
# ac_obj.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
#
#
#
# ele = driver.find_element('xpath', '//h2[text()="SVG Elements"]')
# time.sleep(2)
# ac_obj.scroll_to_element(ele).perform()
#
# draggable_ele = driver.find_element('xpath', '//div[@id="draggable"]')
# time.sleep(2)
# droppable_ele = driver.find_element('xpath', '//div[@id="droppable"]')
# time.sleep(2)
#
# ac_obj.drag_and_drop(draggable_ele, droppable_ele).perform()

###################################################################################################################

# import time
# #
# from selenium import webdriver
#
# from selenium.webdriver.common.action_chains import ActionChains
#
# from selenium.webdriver.common.keys i
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver = webdriver.Chrome()
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@id="name"]').send_keys('jiya')
# time.sleep(2)
#
# ac_obj = ActionChains(driver)
#
# ac_obj.send_keys(Keys.TAB).perform()
# time.sleep(1)
#
# ac_obj.send_keys('jiya@gmail.com').perform()
# time.sleep(2)
#
# ac_obj.send_keys('9786745433').perform()
# time.sleep(2)

############################################################################################################
  ############################### BACKSPACE #########################################

# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@id="name"]').send_keys('susmita')
# time.sleep(2)
#
# ac_obj.send_keys(Keys.BACKSPACE).perform()
# time.sleep(1)
# ac_obj.send_keys(Keys.BACKSPACE).perform()

#####################################################################################################################

####ctrl+a

# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# ac_obj.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL).perform()

####################################################################################################################

       ################################# ctrl + backspace #####################################
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@id="name"]').send_keys('susmita')
# time.sleep(2)
#
# ac_obj.key_down(Keys.CONTROL).send_keys(Keys.BACKSPACE).key_up(Keys.CONTROL).perform()

###################################################################################################################

# driver.get('https://www.facebook.com/r.php?entry_point=login')
# time.sleep(2)
#
# fname = driver.find_element('xpath', '//input[@name="firstname"]')
# lname = driver.find_element('xpath', '//input[@name="lastname"]')
#
# ac_obj = ActionChains(driver)
#
# fname.send_keys('Harry')
# time.sleep(2)
# fname.send_keys('Pottar')
# time.sleep(2)
#


