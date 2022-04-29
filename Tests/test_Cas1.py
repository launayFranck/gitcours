# -*- coding: utf-8 -*-
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import time
import re


class Testingbzh(unittest.TestCase):
#definition du Setup
    def setUp(self):
      
# définition du fichier de log  et son de niveau de sensibilité
        logging.basicConfig(filename='testing_log.log', level=logging.INFO,
                            format='%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s')
# log pour informer de l'évenement
        logging.info('ouverture de chromeDriver')
# lever de l'exception sur le chromedriver
        try:
            self.driver = webdriver.Chrome(executable_path=r"C:\Users\launa\OneDrive\VsCode_Python\chromedriver\chromedriver.exe")
# si problème alors message critique dans le ficher       
        except:
            logging.critical('attention le driver ,n\'pas configuré')
# sinon info sur le bon fonctionnent du driver
        else:logging.info('driver ok!')   
        self.driver.base_url = "https://testing.bzh"
        self.driver.verificationErrors = []
        self.driver.accept_next_alert = True
        self.driver.maximize_window()
        self.driver.implicitly_wait(30) 

    def test_ingbzh(self):
        driver = self.driver
        driver.get(driver.base_url)
        logging.info('ouverture de testing.bzh')
        driver.find_element(by=By.LINK_TEXT, value="Audit et Conseil").click()
        driver.find_element(
            by=By.XPATH, value="//div[@id='post-341']/div[2]/section/div/div").click()
        try:
            self.assertEqual("Audit & Conseil", driver.find_element(by=By.XPATH, value="//div[@id='post-341']/div[2]/section/div/div/div[2]/div/h3").text)
        except:
            logging.warning('oups ca ne va pas le faire')
        else: logging.info('assert Audit & Conseil ok!')
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
