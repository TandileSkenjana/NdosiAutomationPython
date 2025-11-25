import time

from Pages.homePage import HomePage
from utils.readProperties_data import ReadCongig_data


class Test_LoginToNdosi:
    dev_url = ReadCongig_data().getURLS()
    username = ReadCongig_data().getUsername()
    password = ReadCongig_data().getPassword()

    def test_loginWithValidDetails(self,setup):
            self.driver = setup
            self.driver.get(self.dev_url)
            self.driver.maximize_window()
            self.hp= HomePage(self.driver)


            time.sleep(2)
            self.driver.quit()
