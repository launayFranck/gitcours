# Generated by Selenium IDE
import logging
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

class TestTest1():
  def setup_method(self):
    logging.basicConfig(filename='testing1_log.log', level=logging.INFO,
                            format='%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s')
# log pour informer de l'évenement
    logging.info('ouverture de chromeDriver')
# lever de l'exception sur le chromedriver
try: self.driver = webdriver.Chrome(executable_path=r"C:\Users\launa\OneDrive\VsCode_Python\chromedriver\chromedriver.exe")
# si problème alors message critique dans le ficher       
except:
      logging.critical('attention le driver ,n\'pas configure')
# sinon info sur le bon fonctionnent du driver
else:
        logging.info('driver ok!')   
def teardown_method(self, method):
    self.driver.quit()
    
def test_test1(self):
    # Test name: test1
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("https://testing.bzh/")
    # 2 | setWindowSize | 972x796 | 
    self.driver.set_window_size(972, 796)
    # 3 | click | id=cn-accept-cookie | 
    self.driver.find_element(By.ID, "cn-accept-cookie").click()
    # 4 | mouseOver | linkText=Formations | 
    element = self.driver.find_element(By.LINK_TEXT, "Formations")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 5 | assertElementPresent | linkText=Parlons-en ! | 
    elements = self.driver.find_elements(By.LINK_TEXT, "Parlons-en !")
    assert len(elements) > 0
  
