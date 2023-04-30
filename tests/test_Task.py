import time
import pytest


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

        homePage.singInButton()
        singInPage.clickToSingUp()
        creatNewAcountPage.creatNewAccount()
        time.sleep(5)
        coursesPage.chooseFreeCourse()
        courseEnrollPage.enrollCourse()
        courseEnrollPage.assertEnrolling()





