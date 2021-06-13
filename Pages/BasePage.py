import logging

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.Logutils import Logger
from Utilities import configReader


log=Logger(__name__,logging.INFO)

class BasePage():
    def __init__(self, driver):
        self.driver = driver


    def click(self, locator):
        if str(locator).endswith("_xpath"):
            self.driver.find_element_by_xpath(configReader.readconfig("locators", locator)).click()
        elif str(locator).endswith("_css"):
            self.driver.find_element_by_css_selector(configReader.readconfig("locators", locator)).click()
        elif str(locator).endswith("_id"):
            self.driver.find_element_by_id(configReader.readconfig("locators", locator)).click()
        log.logger.info("Clicking on element :"+str(locator))


    def sendkeydata(self, locator, value):
        if str(locator).endswith("_xpath"):
            self.driver.find_element_by_xpath(configReader.readconfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_css"):
            self.driver.find_element_by_css_selector(configReader.readconfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_id"):
            self.driver.find_element_by_id(configReader.readconfig("locators", locator)).send_keys(value)

        log.logger.info("Sending data with"+str(locator)+" as:"+str(value))

    def selectdropdown(self, locator, value):
        if str(locator).endswith("_xpath"):
            dropdown = self.driver.find_element_by_xpath(configReader.readconfig("locators", locator))
        elif str(locator).endswith("_css"):
            dropdown = self.driver.find_element_by_css_selector(configReader.readconfig("locators", locator))
        elif str(locator).endswith("_id"):
            dropdown = self.driver.find_element_by_id(configReader.readconfig("locators", locator))

        select = Select(dropdown)
        select.select_by_visible_text(value)
        log.logger.info("Selecting from an element " + str(locator) + " and value selected as:" + str(value))


    def movetoelement(self,locator):
        if str(locator).endswith("_xpath"):
            ele = self.driver.find_element_by_xpath(configReader.readconfig("locators", locator))
        elif str(locator).endswith("_css"):
            ele = self.driver.find_element_by_css_selector(configReader.readconfig("locators", locator))
        elif str(locator).endswith("_id"):
            ele = self.driver.find_element_by_id(configReader.readconfig("locators", locator))

        act=ActionChains(self.driver)
        act.move_to_element(ele).perform()
        log.logger.info("Moving to an element " + str(locator))


    def verifylinkpresence(self,text):
        wait=WebDriverWait(self.driver,10,poll_frequency=2)
        wait.until(EC.presence_of_element_located((By.XPATH,text)))







