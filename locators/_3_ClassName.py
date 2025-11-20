'''
class name  :   If we are having "class" attribute, we can use "class name" locator

                DRAWBACKS
                .  class name is not unique.
                    In case of multiple occurences, class name locator will always consider the first occurance
                .   class name locator cannot locate the spaces
                    Whenever there is a space in the value of the class attribute, we will replace the space with dot(.)



'''

# import time
#
# from selenium import webdriver
#
# opts =webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(3)
#
# driver.find_element('class name','ico-register').click()
# time.sleep(3)


############################################################3

## NoSuchElementException
## Because class name locator cannot recognize the spaces


# import time
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.facebook.com/r.php?entry_point=login/')
# time.sleep(2)
#
# driver.find_element('class name',"inputtext _58mg _5dba _2ph-").send_keys('jiyu')
# time.sleep(2)



## To overcome the above issue, we have to replace the space with dot(.)


# import time
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.facebook.com/r.php?entry_point=login/')
# time.sleep(2)
#
# driver.find_element('class name',"inputtext._58mg._5dba._2ph-").send_keys('jiyu')
# time.sleep(2)

##########################################################################

## Both the values will be filled in the same textbox

# import time
#
# from selenium import webdriver
#
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Jiya Abbot\OneDrive\pychammfiles\css_selector.html')
# time.sleep(4)
#
# driver.find_element('class name', 'first_row').send_keys('Jiyuu')
# time.sleep(1)
#
# driver.find_element('class name','first_row').send_keys('Abbot')
# time.sleep(1)



