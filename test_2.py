# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTest2():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_test2(self):
    self.driver.get("http://demo-store.seleniumacademy.com/")
    self.driver.set_window_size(974, 1032)
    self.driver.find_element(By.CSS_SELECTOR, ".item:nth-child(2) .product-name > a").click()
    self.driver.find_element(By.CSS_SELECTOR, ".toggle-tabs > li:nth-child(2) > span").click()
    # self.driver.find_element(By.CSS_SELECTOR, ".first > .data").click()
    # self.driver.find_element(By.CSS_SELECTOR, ".even > .data").click()
    # self.driver.find_element(By.CSS_SELECTOR, ".last > .data").click()
    # self.driver.find_element(By.CSS_SELECTOR, ".last:nth-child(3) > span").click()

    price = self.driver.find_element(By.CSS_SELECTOR, "#product-price-421 > .price").text
    assert price[0] == "$"
    assert price == "$210.00"
  
