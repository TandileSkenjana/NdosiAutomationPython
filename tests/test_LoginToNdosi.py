import time

import pytest

from Pages.homePage import HomePage
from Pages.loginPage import LoginPage
from utils.readProperties_data import ReadCongig_data
from utils.commonLogin import loginToNdosi


class Test_LoginToNdosi:
    dev_url = ReadCongig_data().getURLS()
    username = ReadCongig_data().getUsername()
    password = ReadCongig_data().getPassword()

    @pytest.mark.dev
    def test_loginWithValidDetails(self,setup):
            self.driver = setup
            self.driver.get(self.dev_url)
            self.driver.maximize_window()

        #initiate login process
            # self.hp= HomePage(self.driver)
            # self.hp.verifyNdosiHeading()
            # self.hp.clickLearningMaterial()
            # self.login=LoginPage(self.driver)
            # self.login.enterEmail(self.username)
            # self.login.enterPassword(self.password)
            # self.login.clickLoginBtn()
            loginToNdosi(self.driver, self.username, self.password)

            time.sleep(10)
    
    def test_loginWithInvalidDetails(self, setup):
          self.driver = setup
          self.driver.get(self.dev_url)
          self.driver.maximize_window()
          # self.hp = HomePage(self.driver)
          # self.hp.verifyNdosiHeading()
          # self.hp.clickLearningMaterial()
          # self.login = LoginPage(self.driver)
          # self.login.enterEmail(self.username)
          # self.login.enterPassword(self.password+"invalid")
          # self.login.clickLoginBtn()
          loginToNdosi(self.driver, self.username, self.password+"invalid")





           # self.driver.quit()
