from common.base_page import BasePage
from selenium.webdriver.common.by import By
import re

class LPCoursesPage(BasePage):

    def __init__(self):
        super().__init__()

    _ref_item = "//a[@data-id='{0}']"
    _reset_button = "//button[@data-id='3904']"
    _unit_scope = "//div[@class='section-header'][{0}]//b"
    _calculate_button = "//button[contains(.,'Calculate')]"
    _course_scope = "//span[@class='average_score']"

    def click_on_ref_item(self, lesson_id):
        el = self.wait_for_element(By.XPATH, self._ref_item.format(lesson_id))
        self.click_on_element_by_js(el)

    def click_on_reset_button(self):
        el = self.wait_for_element(By.XPATH, self._reset_button)
        self.click_on_element_by_js(el)

    def reset_button_is_displayed(self):
        return self.element_present(self.wait_for_element(By.XPATH, self._reset_button))

    def get_unit_score(self, unit_number):
        scope_text = self.wait_for_element(By.XPATH, self._unit_scope.format((unit_number))).text
        return re.findall('\d+', scope_text)[0]

    def calculate_course_scope(self):
        el = self.wait_for_element(By.XPATH, self._calculate_button)
        self.click_on_element_by_js(el)
        scope_text = self.wait_for_element(By.XPATH, self._course_scope).text
        return re.findall('\d+', scope_text)[0]




