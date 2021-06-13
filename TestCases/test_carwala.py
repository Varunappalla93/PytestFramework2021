import logging
import time
import allure
import openpyxl
import pytest

from Pages.CarBase import CarBase
from Pages.CarHomePage import CarHomePage
from Pages.NewCarsPage import NewCarsPage
from TestCases.BaseTest import BaseTest
from Utilities import dataProvider
from Utilities.Logutils import Logger

log = Logger(__name__, logging.INFO)


class Test_CarWale(BaseTest):
    # @pytest.mark.skip
    def test_gotonewcar(self):
        log.logger.info("***Inside new car test****")
        chp = CarHomePage(self.driver)
        chp.gotonewcars()
        time.sleep(3)

    # @pytest.mark.skip
    @pytest.mark.parametrize("CarBrand", [("BMW")])
    def test_selectcar(self, CarBrand):
        log.logger.info("***Cars select test***")
        chp = CarHomePage(self.driver)
        car = CarBase(self.driver)

        if CarBrand == 'Honda':
            chp.gotonewcars().selectHonda()  # to move to next page using method chaining
            title = car.getCarTitle()
            print(('TITLE IS' + title).encode('utf8'))
            assert title == 'Hondah Cars', 'title is wrong'

        elif CarBrand == 'BMW':
            chp.gotonewcars().selectBMW()
            title = car.getCarTitle()
            print(('TITLE IS ' + title).encode('utf8'))
            assert title == 'BMW Cars', 'title is wrong'

    @pytest.mark.parametrize("CarBrand", [("Honda"),("BMW")])
    def test_getcarnamesandprices(self,CarBrand):
        log.logger.info("***Cars names and prices test***")
        chp = CarHomePage(self.driver)
        car = CarBase(self.driver)
        if CarBrand == 'Honda':
            chp.gotonewcars().selectHonda()
            title = car.getCarTitle()
            assert title == 'Honda Cars', 'title is wrong'
            car.getCarNameandPrice()

        if CarBrand == 'BMW':
            chp.gotonewcars().selectBMW()
            title = car.getCarTitle()
            assert title == 'BMW Cars', 'title is wrong'
            car.getCarNameandPrice()
