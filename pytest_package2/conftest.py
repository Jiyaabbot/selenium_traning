'''

conftest = configration test file

* we don't have import conftest file
* I don't have Setups or connection b/w conftest file and test file.
* In conftest whatever we code writen automaticaaly it will be applied all the present file inside the pytest_package.

 ** to excute next file we us --- python -m pytest -vs

 ** THIS excution we called as batch exceution.
'''

# import time
#
# import pytest
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# @pytest.fixture(scope='class')
# def setup():
#     driver = webdriver.Chrome(opts)
#     driver.get("https://demowebshop.tricentis.com/")
#     time.sleep(2)
#     yield driver
#     driver.close()