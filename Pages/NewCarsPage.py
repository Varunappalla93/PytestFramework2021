from Pages.BasePage import BasePage


class NewCarsPage(BasePage):  # Inheritance
    def __init__(self, driver):
        super().__init__(driver) # comes from BasePage


    def selectHyundai(self):
        self.click("hyundai_xpath")

    def selectToyota(self):
        self.click("toyota_xpath")

    def selectBMW(self):
        self.click("Bmw_xpath")

    def selectHonda(self):
        self.click("honda_xpath")


