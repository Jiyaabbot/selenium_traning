'''
Alerts  :   Alerts are not inspectable.
            Suppose if we are able to inspect, then it is not an alert.

            To handle the alerts, we will switch the driver to the alert
            SYNTAX  :   alert_obj = driver.switch_to.alert
                        alert_obj has two attributes to handle the alert
                        *   accept()    :   To accept the alert, we use alert_obj.accept()
                        *   dismiss()   :   To dismiss the alert, we use alert_obj.dismiss()

            There are different types alerts
            *   simple alert    :   If the alert is having only one option, then it is a simple alert.
                                    To handle the simple alert, first switch the driver to the alert
                                    Now we can either use accept or dismiss.
                                    alert_obj.accept()  or      alert_obj.dismiss()

            *   confirmation alert  :   If the alert is having two options, then it is a confirmation alert.
                                    To handle the confirmation alert, first switch the driver to the alert
                                    To click on OK/YES/AGREE,.. we give alert_obj.accept()
                                    To click on CANCEL/NO/DISAGREE,.. we give alert_obj.dismiss()

            *   Prompt alert    :   Here the alert will take the data from the user.
                                    To handle the prompt alert, first switch the driver to the alert
                                    alert_obj.send_keys("data")
                                    alert_obj.accept()



'''



#simple alert

import time

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver = webdriver.Chrome(opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(3)
#
# driver.find_element('xpath','//button[text()="Simple Alert"]').click()
# time.sleep(2)
#
# alert_obj = driver.switch_to.alert
#
# alert_obj.accept()
# time.sleep(1)


################################################################################################


## conformation alert

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver = webdriver.Chrome(opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# driver.find_element('xpath','//button[text()="Confirmation Alert"]').click()
# time.sleep(2)
#
# ## switch the driver to the alert
# alert_obj = driver.switch_to.alert
# ## To click on OK/YES/AGREE,
# alert_obj.accept()
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Confirmation Alert"]').click()
# ## switch the driver to the alert
# alert_obj = driver.switch_to.alert
#
# ## To click on CANCEL/NO/DISAGREE,
# alert_obj.dismiss()
# time.sleep(2)

###################################################################################################


# prompt alert


# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver = webdriver.Chrome(opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(3)
#
# driver.find_element('xpath','//button[text()="Prompt Alert"]').click()
# time.sleep(2)
#
# alert_obj = driver.switch_to.alert
#
# alert_obj.send_keys('Jiya')
# alert_obj.accept()

######################################################################################


##################################  Authentication pop-ups ###############################################

##The above url will give a pop-up which will ask for the username and password to launch the application.
# It is not inspectable

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://the-internet.herokuapp.com/basic_auth/')
# time.sleep(2)



# The above url will give a pop-up which will ask for the username and password to launch the application.
# It is not inspectable

#############################################################################################

## To handle such pop-ups, we will give the username and password in the url while launching the application
## SYNTAX   :   https://username:password@url

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')
# time.sleep(2)

##############################################################################################

################################# file-upload pop-up###############################3

##single-file upload

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver = webdriver.Chrome(opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
#
# choose_file = driver.find_element("xpath",'//input[@id="singleFileInput"]')
# File_path = r'C:\Users\Jiya Abbot\PycharmProjects\selenium_traning\files\loading.html'
#
# choose_file.send_keys(File_path)

#######################################################################################################################
################################ multiple-file upload ##########################################################

# from selenium import webdriver
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver = webdriver.Chrome(opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
#
# multiple_files = driver.find_element('xpath', '//input[@id="multipleFilesInput"]')
# time.sleep(1)
#
# f1= r'C:\Users\Jiya Abbot\PycharmProjects\selenium_traning\files\progressbar.html'
# f2= r'C:\Users\Jiya Abbot\PycharmProjects\selenium_traning\css_selector.html'
# f3= r'C:\Users\Jiya Abbot\PycharmProjects\selenium_traning\demo.html'
#
# multiple_files.send_keys(f'{f1}\n{f2}\n{f3}')

#########################################################################################################

############################## push notifications ###########################################


# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
#
# opts.add_argument('--disable-notification')
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.irctc.co.in/nget/train-search')
#















