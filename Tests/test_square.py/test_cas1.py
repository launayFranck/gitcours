# -*- coding: utf-8 -*-
import logging
import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException


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
            logging.critical('attention le driver ,n\'pas configure')
# sinon info sur le bon fonctionnent du driver
        else:logging.info('driver ok!')   
        #self.driver.base_url = "https://testing.bzh"
        logging.info('le site est ouvert')
        #self.driver.verificationErrors = []
        #self.driver.accept_next_alert = True
        self.driver.maximize_window()
        self.driver.implicitly_wait(30) 

    def test_ingbzh(self):
        driver = self.driver
        self.driver.get("https://testing.bzh")
        try:
            assert driver.current_url == "https://testing.bzh"
            assert driver.title == 'Testing-BZH'
            logging.info('ouverture de testing.bzh')
            driver.find_element(by=By.LINK_TEXT, value="Audit et Conseil").click()
            driver.find_element(by=By.XPATH, value="//div[@id='post-341']/div[2]/section/div/div").click()
            
        except : logging.warning( 'attention la page ne s\'affiche pas sur tesing.bzh')

        else :
          def tearDown(self):
           self.driver.quit()
           self.assertEqual([], self.verificationErrors)
if __name__ == "__main__":
 unittest.main()
