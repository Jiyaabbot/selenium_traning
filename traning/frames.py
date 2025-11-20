# '''
# iframe  :   It is an inline-frame
#             The web-application inside another application is an iframe.
#
#             The tagname of an iframe is always "iframe"
#
#             To handle the iframes
#             *   Locate the frame
#             *   Switch the driver to the frame
#                 SYNTAX  :   driver.switch_to.frame(frame)
#             *   Perform the operations inside the frame
#             *   Once after performing the oprations inside the frame, switch back to the parent frame
#                 SYNTAX  :   driver.switch_to.parent_frame()
#
# '''
#
# import time
# #
# # from selenium import webdriver
# #
# # from selenium.webdriver.common.action_chains import ActionChains
# #
# # opts = webdriver.ChromeOptions()
# # opts.add_experimental_option("detach",True)
# # driver = webdriver.Chrome(opts)
# # ac_obj = ActionChains(driver)
# #
# # driver.get('https://www.linkedin.com/')
# # time.sleep(2)
# #
# #
# # # ## locate the iframe
# # google_frame = driver.find_element("xpath",'//iframe[@title="Sign in with Google Button"]')
# #
# # # ## switch the driver to the frame
# # driver.switch_to.frame(google_frame)
# # time.sleep(2)
# #
# # # ## perform the operations inside the frame
# # driver.find_element("xpath",'//span[text()="Continue with Google"]').click()
# # time.sleep(2)
# #
# # # ## switch back to the parent frame
# # driver.switch_to.parent_frame()
# #
# # # ## scroll down until youtube_frame is visible
# # ele = driver.find_element("xpath",'//h2[contains(text(), "Join your colleagues")]')
# #
# # ac_obj.scroll_to_element(ele).perform()
# # time.sleep(2)
# #
# # #locate the youtube_frame
# # youtube_frame = driver.find_element("xpath",'//iframe[@title="Gayatri Iyer: In it to chase my dream | #InItTogether"]')
# #
# # # ## switch the driver to the youtube_frame
# # driver.switch_to.frame(youtube_frame)
# # time.sleep(2)
# #
# # # ## perform the operations in the youtube_frame
# # driver.find_element("xpath",'//button[@title="Play"]').click()
# # time.sleep(5)
# #
# # ## switch back to the parent frame
# # driver.switch_to.parent_frame()
# # time.sleep(2)
# #
# # driver.close()
#
# #####################################################################################################################
#
# ####Eg1
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# ac_obj = ActionChains(driver)
#
# driver.get('https://www.linkedin.com')
# time.sleep(2)
#
# f2 = driver.find_element('xpath', '//iframe[@name="microsoft_signin_iframe_1"]')
# driver.switch_to.frame

##################################################################################################################
