from selenium.webdriver.common.by import By
from faker import Faker

class CreateNewAccountPage:
    def __init__(self, driver):
        self.driver = driver

    FIRSTNAME_BOX = (By.XPATH,".//input[@id='user[first_name]']")
    LASTNAME_BOX = (By.XPATH, ".//input[@id='user[last_name]']")
    EMAIL_BOX = (By.XPATH, ".//input[@id='user[email]']")
    PASSWORD_BOX = (By.XPATH, ".//input[@id='user[password]']")
    CHECK_BOX = (By.XPATH, "//input[@id='user[terms]']")
    CREATE_BUTTON = (By.XPATH, "//button[@class='button button-primary g-recaptcha']")

    def creatNewAccount(self):
        fake=Faker()

        self.driver.find_element(*CreateNewAccountPage.FIRSTNAME_BOX).send_keys(fake.first_name())
        self.driver.find_element(*CreateNewAccountPage.LASTNAME_BOX).send_keys(fake.last_name())
        self.driver.find_element(*CreateNewAccountPage.EMAIL_BOX).send_keys(fake.email())
        self.driver.find_element(*CreateNewAccountPage.PASSWORD_BOX).send_keys(fake.password())
        self.driver.find_element(*CreateNewAccountPage.CHECK_BOX).click()
        self.driver.find_element(*CreateNewAccountPage.CREATE_BUTTON).click()