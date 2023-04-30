from selenium.webdriver.common.by import By

from utilities.PageBase import PageBase


class CourseEnrollPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ENROLL_BUTTON = (By.XPATH, "//a[text()='Enroll for free']")
    ENROLL_MESSAGE = (By.XPATH, "//p[@class='message-text']")

    def enrollCourse(self):
        click_enroll_button=self.wait_element_visibility(CourseEnrollPage.ENROLL_BUTTON)
        click_enroll_button.click()

    def assertEnrolling(self):
        self.driver.back()
        result = self.wait_element_visibility(CourseEnrollPage.ENROLL_MESSAGE)
        assert result.text == "Successfully enrolled you in the course"


