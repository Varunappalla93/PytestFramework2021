from Pages.BasePage import BasePage
from Utilities import configReader


class HondaPage(BasePage):  # Inheritance
    def __init__(self, driver):
        super().__init__(driver) # comes from BasePage
