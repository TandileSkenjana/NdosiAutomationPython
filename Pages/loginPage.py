from selenium.webdriver.common.by import By


class LoginPage:
    lbl_enterEmail_id = "login-email"

    def __init__(self, driver):
        self.driver = driver
# added method to enter email
    def enterEmail(self, email):
        element = self.driver.find_element(By.ID, self.txt_email_id)
        element.send_keys(email)