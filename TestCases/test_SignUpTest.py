# to generate screenshot based on failure
import logging

import allure
import openpyxl
import pytest
from TestCases.BaseTest import BaseTest
from Utilities import dataProvider
from Pages.RegistrationPage import Registration
from Utilities.Logutils import Logger



log=Logger(__name__,logging.INFO)

class Test_SignUpTest(BaseTest):

    @pytest.mark.parametrize("name, phoneno, email, countryname, city, username, password", dataProvider.getdata("LoginTest"))
    def test_DoSignup(self, name, phoneno, email, countryname, city, username, password):
        log.logger.info("Test Do Signup started")
        rp=Registration(self.driver)
        rp.fillform(name, phoneno, email, countryname, city, username, password)
        log.logger.info("Test Do Signup finished")

