from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
       self.driver = driver

    SING_IN_BUTTON = (By.XPATH, ".//a[@href='/users/sign_in']")
    def singInButton(self):
        self.driver.find_element(*HomePage.SING_IN_BUTTON).click()