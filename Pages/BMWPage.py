from Pages.BasePage import BasePage


class BMW(BasePage):  # Inheritance
    def __init__(self, driver):
        super().__init__(driver) # comes from BasePage