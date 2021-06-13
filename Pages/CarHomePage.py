from Pages.BasePage import BasePage
from Pages.NewCarsPage import NewCarsPage


class CarHomePage(BasePage):  # Inheritance
    def __init__(self, driver):
        super().__init__(driver) # comes from BasePage


    def gotonewcars(self):
        self.movetoelement("newCar_xpath")
        self.click("findNewCars_xpath")

        return NewCarsPage(self.driver) # next page chaining for its methods



    def comparecars(self):
        pass


    def gotousedcars(self):
        pass


