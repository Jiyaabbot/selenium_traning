# parameters = cross browsing

# import time
#
# import pytest
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# @pytest.fixture(scope='class', params=['chrome', 'firefox', 'edge'])     # params = plural
# def setup(request):
#     parameter = request.param       ## parameter = edge                  # param = singulare
#
#     if parameter == 'chrome':
#         driver = webdriver.Chrome(opts)
#     elif parameter == 'firefox':
#         driver = webdriver.Firefox()
#     elif parameter == 'edge':
#         driver = webdriver.Edge()
#
#     driver.get("https://demowebshop.tricentis.com/")
#     time.sleep(2)
#     yield driver
#     driver.close()
#
# class TestRegister:
#
#     def test_reg_link(self, setup):
#         setup.find_element('xpath', '//a[text()="Register"]').click()
#         time.sleep(2)
#
#     def test_gender_btn(self, setup):
#         setup.find_element('id', 'gender-male').click()
#
#     def test_fname(self, setup):
#         setup.find_element('id', 'FirstName').send_keys('jiya')
#
#     def test_lname(self, setup):
#         setup.find_element('id', 'LastName').send_keys('abbot')
#
#     def test_reg_email(self, setup):
#         setup.find_element('id', 'Email').send_keys('jiya@gmail.com')
#
#     def test_reg_pwd(self, setup):
#         setup.find_element('id', 'Password').send_keys('jiya@12345')
#
#     def test_confirm_pwd(self, setup):
#         setup.find_element('id', 'ConfirmPassword').send_keys('jiya@12345')
#
# class TestLogin:
#
#     def test_login_link(self, setup):
#         setup.find_element('xpath', '//a[text()="Log in"]').click()
#         time.sleep(2)
#
#     def test_login_email(self, setup):
#         setup.find_element('id', 'Email').send_keys('jiya@gmail.com')
#
#     def test_login_pwd(self, setup):
#         setup.find_element('id', 'Password').send_keys('jiya@12345')
