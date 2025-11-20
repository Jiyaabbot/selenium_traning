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
# footer_elements = driver.find_elements('xpath', '//div[@class="footer-menu-wrapper"]//a')
# # print(footer_elements)      ## list of web-elements         ## [wb1, wb2, wb3, wb4, wb5, wb6, wb7,...wb22]
#
# for ele in footer_elements:
#     print(ele.text)

##############################################################################################################

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
# categories = driver.find_elements('xpath', '//div[@class="block block-category-navigation"]//a')
# print(categories)       ## list of web-elements         ## [wb1, wb2, wb3, wb4, wb5, wb6, wb7]
#
# for ele in categories:
#     print(ele.text)

###########################################################################################################################

#from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# popular_searches = driver.find_elements('xpath', '//div[@class="desktop-pSearchlinks"]//a')
# # print(popular_searches)         ## list of web-elements         ## [wb1, wb2, wb3, wb4, wb5, wb6,...wb47]
#
# for ele in popular_searches:
#     print(ele.text)

#############################################################################################################

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.python.org/')
# time.sleep(2)
#
# '''
# all links --> href --> anchor tags
# '''
#
# all_links = driver.find_elements('tag name', 'a')
# # print(all_links)       ## list of web-elements      ## [a1, a2, a3, a4, a5,...]
#
# for link in all_links:
#     print(link.get_attribute('href'))

###################################################################################################################

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.python.org/')
# time.sleep(2)
#
# '''
# all links --> href --> anchor tags
# '''
#
# all_links = driver.find_elements('tag name', 'a')
# # print(all_links)       ## list of web-elements      ## [a1, a2, a3, a4, a5,...]
#
# for link in all_links:
#     print(link.get_attribute('href'))