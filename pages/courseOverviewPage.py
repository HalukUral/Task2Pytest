from selenium.webdriver.common.by import By


class CourseOverviewPage:
    def __init__(self, driver):
        self.driver = driver

    def goDashbordPage(self):
        self.driver.find_element(By.XPATH, "(//a[starts-with(@href, '/enrollments')])[1]").click()