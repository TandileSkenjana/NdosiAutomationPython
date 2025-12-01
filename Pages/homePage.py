from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    lbl_Heading_id = "overview-hero"
    btn_learningMaterial_id = "nav-btn-practice"

    def __init__(self, driver):
        self.driver = driver

    def verifyNdosiHeading(self):
        """Wait for the heading to be visible and return True/False."""
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.ID, self.lbl_Heading_id)))
        return element.is_displayed()

    def clickLearningMaterial(self, timeout=10):
        """Wait for the learning material button to be clickable and click it."""
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.btn_learningMaterial_id)))
        element.click()
