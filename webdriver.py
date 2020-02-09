import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class WebDriverPythonBasics():

    def __init__(self):
        self.browser = webdriver.Chrome(executable_path='/Users/roshy/Documents/chromedriver')
        self.url = 'https://www.youtube.com'

    def open_website(self):
        self.browser.get(self.url)
        self.scan_for_advert()
        self.utube_btn_class = 'ytp-ad-skip-button'

    def scan_for_advert(self):
        while True:
            time.sleep(5)
            if(self.is_advert()):
                self.skip_advert()

    def is_advert(self):
        try:
            element = self.browser.find_element_by_class_name(self.utube_btn_class)
            return element.is_displayed()
        except:
            print ('that element doesnt exists at the moment')
            return False

    def skip_advert(self):
        element = self.browser.find_element_by_class_name(self.utube_btn_class)
        element.click()
        print('clicked `skip advert`')

wd = WebDriverPythonBasics()
wd.open_website()