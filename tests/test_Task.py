import time

import pytest
from selenium.webdriver.common.by import By

from pages.courseOverviewPage import CourseOverviewPage
from pages.coursesPage import CoursesPage
from pages.createNewAccountPage import CreateNewAccountPage
from pages.HomePage import HomePage
from pages.SingInPage import SingInPage
from pages.courseEnrollPage import CourseEnrollPage


@pytest.mark.usefixtures("setup")
class TestTask:
    def test_taskStep(self):
        homePage=HomePage(self.driver)
        singInPage=SingInPage(self.driver)
        creatNewAcountPage=CreateNewAccountPage(self.driver)
        coursesPage=CoursesPage(self.driver)
        courseEnrollPage=CourseEnrollPage(self.driver)
        courseOverviewPage=CourseOverviewPage(self.driver)

        homePage.singInButton()
        singInPage.clickToSingUp()
        creatNewAcountPage.creatNewAccount()

        time.sleep(10)
        coursesPage.chooseFreeCourse()
        courseEnrollPage.enrollCourse()
        courseEnrollPage.assertEnrolling()





