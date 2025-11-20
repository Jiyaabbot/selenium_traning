# # # import time
# # #
# # # from selenium import webdriver
# # #
# # # opts = webdriver.ChromeOptions()
# # # opts.add_experimental_option("detach", True)
# # #
# # # driver = webdriver.Chrome(opts)
# # #
# # # driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-E19-7PM-Aug28-2025\files\loading.html')
# # # time.sleep(20)
# # #
# # # driver.find_element('xpath', '//input[@name="fname"]').send_keys('Mounika')
# # # time.sleep(1)
# # # driver.find_element('xpath', '//input[@name="lname"]').send_keys('KM')
# #
# # ###########################################################################################################33333
# #
# # ################################# implicit_wait ##############################################
# #
# # #from selenium import webdriver
# # #
# # # opts = webdriver.ChromeOptions()
# # # opts.add_experimental_option("detach", True)
# # #
# # # driver = webdriver.Chrome(opts)
# # #
# # # driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-E19-7PM-Aug28-2025\files\loading.html')
# # # driver.implicitly_wait(30)
# # #
# # # driver.find_element('xpath', '//input[@name="fname"]').send_keys('Mounika')
# # # time.sleep(1)
# # # driver.find_element('xpath', '//input[@name="lname"]').send_keys('KM')
# #
# # ##################################################################################################################
# #
# # ############################ explicit_wait #########################################
# #
# # # from selenium import webdriver
# # # from selenium.webdriver.support.ui import WebDriverWait
# # # from selenium.webdriver.support import expected_conditions
# # #
# # # opts = webdriver.ChromeOptions()
# # # opts.add_experimental_option("detach", True)
# # #
# # # driver = webdriver.Chrome(opts)
# # #
# # # wait_obj = WebDriverWait(driver, 10)
# # #
# # # driver.get('https://www.saucedemo.com/')
# # # time.sleep(2)
# # # driver.find_element('xpath', '//input[@id="user-name"]').send_keys('standard_user')
# # # time.sleep(1)
# # # driver.find_element('xpath', '//input[@id="password"]').send_keys('secret_sauceeeeeeeee')
# # # time.sleep(1)
# # # driver.find_element('xpath', '//input[@id="login-button"]').click()
# # # time.sleep(2)
# # #
# # # try:
# # #     wait_obj.until(expected_conditions.visibility_of_element_located(('xpath', '//span[text()="Products"]')))
# # #     print("successfull login")
# # # except:
# # #     print("unsuccesfull login")
# #
# # ######################################################################################################################
# # ###################################### unconditional synchronization ##############################################
# # #
# # import time
# #
# # from selenium import webdriver
# #
# # opts = webdriver.ChromeOptions()
# # opts.add_experimental_option("detach", True)
# #
# # driver = webdriver.Chrome(opts)
# #
# # driver.get(r'C:\Users\Jiya Abbot\PycharmProjects\selenium_traning\files\progressbar.html')
# # time.sleep(2)
# #
# # driver.find_element('xpath', '//button[text()="Click Me"]').click()
# # time.sleep(40)
# # driver.find_element('xpath', '//button[text()="Click Me"]').click()
# #
# ###########################################################################################################################
# ################################## conditional synchronization ############################
#
# import time
#
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# wait_obj = WebDriverWait(driver, 45)
# driver.get(r'C:\Users\Jiya Abbot\PycharmProjects\selenium_traning\files\progressbar.html')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Click Me"]').click()
#
# wait_obj.until(expected_conditions.visibility_of_element_located(('xpath', '//div[text()="100%"]')))
# time.sleep(1)
#
# driver.find_element('xpath', '//button[text()="Click Me"]').click()
# time.sleep(2)
#
