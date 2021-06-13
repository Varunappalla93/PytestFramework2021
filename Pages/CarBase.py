from Pages.BasePage import BasePage
from Utilities import configReader


class CarBase(BasePage):  # Inheritance
    def __init__(self, driver):
        super().__init__(driver)  # comes from BasePage

    def getCarTitle(self):
        return self.driver.find_element_by_xpath(configReader.readconfig("locators", "carTitle_XPATH")).text

    def getCarNameandPrice(self):
        carnames = self.driver.find_elements_by_xpath(configReader.readconfig("locators", "carName_XPATH"))
        carprices = self.driver.find_elements_by_xpath(configReader.readconfig("locators", "carPrice_XPATH"))

        for i in range(0, len(carprices)):
            print((carnames[i].text + "car prices are" + carprices[i].text).encode('utf8'))


