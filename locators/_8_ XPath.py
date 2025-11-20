'''
xpath   :   It is a locator to locate any element on the application uniquely.
            Using xpath, we can locate the web elements using attributes, using text, can do indexing, can locate
            dynamically changing elements.
            We can locate any element on the application using xpath

            There are 2 types of xpath
            *   Absolute xpath  :   Starts from the root of html
                                    We use / to write the absolute xpath
                                    / represents immediate child

                                    DRAWBACKS
                                    *   Depends on the full path from the root
                                    *   Difficult to maintain
                                    *   Not reusable
                                    *   Not readable
                                    *   Very lengthy and time consuming

            *   Relative xpath  :   Doesnot start from the root of html
                                    We use // to write relative xpath
                                    // represents any child


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
# driver.find_element('xpath', 'html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('xpath', 'html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input').send_keys('secret_sauce')
# time.sleep(1)
# driver.find_element('xpath', 'html/body/div/div/div[2]/div[1]/div/div/form/input').click()



###########################################################################################################


# '''
# attribute name and value    :   //tagname[@attr_name="attr_value"]
#                                 @ represents attribute
#
# '''





# import time
#
# from selenium import webdriver
#
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
#
# driver= webdriver.Chrome(opts)
#
# driver.get('https://www.instagram.com/accounts/emailsignup/')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@aria-label="Mobile Number or Email"]').send_keys('harry@gmail.com')
# time.sleep(1)
# driver.find_element('xpath', '//input[@type="password"]').send_keys('harry@12345')
# time.sleep(1)
# driver.find_element('xpath', '//input[@name="fullName"]').send_keys('harry_potter')
# time.sleep(1)
# driver.find_element('xpath', '//input[@name="username"]').send_keys('harry_12345678')
#

###########################################################################################################

# import time
#
# from selenium import webdriver
#
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
#
# driver= webdriver.Chrome(opts)
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# driver.find_element("xpath",'//a[@data-group="men"]').click()
# time.sleep(2)
#
# driver.find_element("xpath",'//a[@data-group="beauty"]').click()
# time.sleep(2)
#
# driver.find_element('xpath', '//a[@data-group="genz"]').click()
# time.sleep(2)



########################################################################################################

# import time
#
# from selenium import webdriver
#
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
#
# driver= webdriver.Chrome(opts)
#
# driver.get('https://www.youtube.com')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@name="search_query"]').send_keys('Artlifejiyu')
# time.sleep(2)
# driver.find_element('xpath', '//button[@title="Search"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[@id="video-title"]').click()


###############################################################################################################

#import time

from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@id="user-name"]').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('xpath', '//input[@placeholder="Password"]').send_keys('secret_sauce')
# time.sleep(1)
# driver.find_element('xpath', '//input[@value="Login"]').click()
# time.sleep(3)
# driver.find_element('xpath', '//button[@id="react-burger-menu-btn"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[@id="logout_sidebar_link"]').click()

######################################################################################################################


#import time


#from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://www.hotstar.com/')
# time.sleep(3)
# driver.find_element('xpath', '//button[@data-testid="modal-close-button"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[@aria-label="Search"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//input[@id="searchBar"]').send_keys('RRR')


###################################################################################################3

#import time

from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://www.ajio.com/')
# time.sleep(2)
# driver.find_element('xpath', '//a[@title="WOMEN"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[@title="KIDS"]').click()


###########################################################################################################


# '''
# text    :   //tagname[text()="text"]
#
#
# '''

#
# import time
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.flipkart.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//span[text()="Mobiles & Tablets"]').click()
# time.sleep(2)
#
# driver.find_element('xpath', '//span[text()="Become a Seller"]').click()
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Start Selling"]').click()


#############################################################################################################

# import time
#
# from selenium import webdriver
#
# driver = webdriver.Firefox()
#
# driver.get('https://www2.hm.com/en_in/index.html')
# time.sleep(4)
#
# driver.find_element('xpath', '//a[text()="Ladies"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="Kids"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="Home"]').click()
# time.sleep(2)

##############################################################################################################


# import time
#
# from selenium import webdriver
#
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Women"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="Beauty"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="Genz"]').click()


#######################################################################################################################

# '''
#
# Group indexing  :   (any_xpath)[index_num]
# If we dont give any index number, by default it will always consider the first occurance
#
#''



# import time
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
# driver.find_element('xpath', '(//a[@class="desktop-main"])[2]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//a[@class="desktop-main"])[4]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//a[@class="desktop-main"])[6]').click()
# time.sleep(2)

####################################################################################################3

# import time
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Jiya Abbot\PycharmProjects\selenium_traning\css_selector.html')
# time.sleep(2)
#
# driver.find_element('xpath', '(//input[@name="fname"])[1]').send_keys('Joey')
# time.sleep(1)
# driver.find_element('xpath', '(//input[@name="fname"])[2]').send_keys('Chandler')
# time.sleep(1)
# driver.find_element('xpath', '(//input[@name="fname"])[3]').send_keys('Ross')
# time.sleep(2)

######################################################################################################

# import time
#
# from selenium import webdriver
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.python.org/')
# time.sleep(2)
#
# driver.find_element('xpath', '(//a[text()="Downloads"])[2]').click()
# time.sleep(2)

####################################################################################################################3

# '''
# contains    :   To locate the partial portion of the complete text of any tagname
#                 SYNTAX  :   //tagname[contains(text(), "partial_text")]
#
# ''

# import time
#
# from selenium import webdriver
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.giva.co/')
# time.sleep(2)
#
# driver.find_element('xpath', '//span[contains(text(), "Gold with Lab Diamonds")]').click()
# time.sleep(2)
#
# driver.find_element('xpath', '//span[contains(text(), "GIVA Gift Card")]').click()
# time.sleep(2)

#################################################################################################

# import time
#
# from selenium import webdriver
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
#
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '(//a[contains(text(), "Books")])[3]').click()
# time.sleep(2)
#
# driver.find_element('xpath', '(//a[contains(text(), "Computers")])[3]').click()
# time.sleep(2)
#
# driver.find_element('xpath', '(//a[contains(text(), "Electronics")])[3]').click()
# time.sleep(2)
#
# driver.close()

