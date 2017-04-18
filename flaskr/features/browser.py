
from selenium import webdriver
import os


class Browser(object):

    base_url = 'http://localhost:8000'
    chromedriver = "D:/Python/flaskr/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    def close(self):
        self.driver.quit()

    def visit(self, location=''):
        url = self.base_url + location
        self.driver.get(url)

    def find_by_id(self, selector):
        return self.driver.find_element_by_id(selector)


