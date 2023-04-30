from selenium.webdriver.common.by import By


class CoursesPage:
    def __init__(self, driver):
        self.driver = driver
    SELECT_FIRSTFREE_COURSE = (By.XPATH, "(//span[@class='card__badge card__badge--free'])[1]")
    def chooseFreeCourse(self):
        self.driver.find_element(*CoursesPage.SELECT_FIRSTFREE_COURSE).click()
