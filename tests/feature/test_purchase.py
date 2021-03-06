import os

from common.base_test import BaseTest
import pytest
from pages.page_manager import PageManager
import allure
from ddt import ddt, data, unpack
from utilities.recognize_csv import recognizeCSVData
import unittest

unittest.TestCase

@allure.feature("Purchase")
@pytest.mark.usefixtures("user_admin","classSetup")
@ddt
class TestPurchaseClass(unittest.TestCase):

    @pytest.fixture(scope="class")
    def classSetup(self, request, page_manager_set_up):
        # driver = driver_set_up.instance
        pageManager = page_manager_set_up
        if request.cls is not None:
            request.cls.pageManager = pageManager
        with allure.step("log in on site"):
            pageManager.login.logIn_on_site(self.login, self.password)
        yield
        with allure.step("log Out"):
            pageManager.login.delete_cookie()

    @allure.story("To purchase course")
    @data(*recognizeCSVData(os.path.dirname(__file__).partition("/myTEFL/")[0] + "/myTEFL/resourses/testdata.csv"))
    @unpack
    def test_purchase_course(self, expected_result, cc_number, cc_exp_month, cc_exp_year, cc_cvv):
        pm = self.pageManager
        pm.login.go_to('https://dev.mytefl.com/online-onsite-courses/online-tefl-courses/')
        with allure.step("select professional course"):
            pm.select_course.click_on_professional_course_button()
        with allure.step("click on enroll course button"):
            pm.select_course.click_on_enroll_button()
        with allure.step("scroll page to card payment form"):
            pm.check_out.scroll_to_element(pm.check_out.get_payment_form())
        with allure.step("click on a checkbox"):
            pm.check_out.click_on_term_checkBox()
        with allure.step("fill card payment form"):
            pm.check_out.fill_card_form(cc_number, cc_exp_month, cc_exp_year, cc_cvv)
        with allure.step("course purchase"):
            pm.check_out.click_on_order_button()
        with allure.step("chek out a result"):
            self.assertEqual(int(expected_result),pm.check_out.check_out_purchase_result(expected_result))