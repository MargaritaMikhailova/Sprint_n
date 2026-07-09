import allure

from locators import Elements_check
from pages.base_page import BasePage


class SelectorPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Ожидание загрузки выбора маршрута")
    def wait_selector_menu_page(self):
        return self.find_long_element(Elements_check.MENU_PAGE)

    @allure.step("Посмотреть блок информации Стоимость")
    def check_amount_block(self):
        return self.find_long_element(Elements_check.AMOUNT_ROUTE)

    @allure.step("Посмотреть блок информации Время в пути")
    def check_time_block(self):
        return self.find_long_element(Elements_check.TIME_ROUTE)
