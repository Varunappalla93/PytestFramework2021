from selenium.webdriver.support.select import Select

from Pages.BasePage import BasePage
from Utilities import configReader


class Registration(BasePage):  # Inheritance
    def __init__(self, driver):
        super().__init__(driver) # comes from BasePage
        # self.driver = driver


    def fillform(self, name, phoneno, mail, countryname, city, username, password):
        self.sendkeydata("name_xpath",name)  # comes from Base Page methods
        self.sendkeydata("phone_css", phoneno)
        self.sendkeydata("email_xpath", mail)

        self.selectdropdown("country_xpath",countryname)

        self.sendkeydata("city_xpath", city)
        self.sendkeydata("username_xpath",username)
        self.sendkeydata("password_xpath", password)

        self.click("submit_xpath")




        # General approach
        # self.driver.find_element_by_xpath(configReader.readconfig("locators", "name_xpath")).send_keys(name)
        # self.driver.find_element_by_xpath(configReader.readconfig("", "")).send_keys(no)
        # self.driver.find_element_by_xpath(configReader.readconfig("", "")).send_keys(mail)
        #
        # drpdwn =self.driver.find_element_by_xpath(configReader.readconfig("", "")).send_keys(countryname)
        # select=Select(drpdwn)
        # select.select_by_visible_text(countryname)
        #
        # self.driver.find_element_by_xpath(configReader.readconfig("locators", "name_xpath")).send_keys(city)
        # self.driver.find_element_by_xpath(configReader.readconfig("", "")).send_keys(username)
        # self.driver.find_element_by_xpath(configReader.readconfig("", "")).send_keys(password)












