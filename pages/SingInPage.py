from selenium.webdriver.common.by import By


class SingInPage:
    def __init__(self, driver):
        self.driver = driver

    SING_UP_BUTTON = (By.XPATH, ".//a[@href='/users/sign_up']")
    def clickToSingUp(self):
        self.driver.find_element(*SingInPage.SING_UP_BUTTON).click()