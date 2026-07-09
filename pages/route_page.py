import allure

from locators import Elements_check
from pages.base_page import BasePage
from data import Data


class RoutePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Ожидание загрузки Войти на сайт")
    def wait_for_load_page(self):
        return self.find_long_element(Elements_check.MAP_PAGE)

    @allure.step("Получение текущего URL")
    def get_current_url_login_page(self):
        return self.get_current_url_page()

    @allure.step("Ожидание загрузки меню слева")
    def wait_load_menu_page(self):
        return self.find_long_element(Elements_check.MENU_PAGE)

    @allure.step("Заполнение формы карты Откуда")
    def fill_data_route_from(self):
        self.input_text(Elements_check.ADDRESS_CONTAINER_FROM, Data.ADDRESS_1[0])

    @allure.step("Заполнение формы карты Куда")
    def fill_data_route_to(self):
        self.input_text(Elements_check.ADDRESS_CONTAINER_TO, Data.ADDRESS_2[0])

    @allure.step("Отображаение точки А на карте")
    def wait_point_exist_a(self):
        return self.find_long_element(Elements_check.TOCHKA_A)

    @allure.step("Отображаение точки В на карте")
    def wait_point_exist_b(self):
        return self.find_long_element(Elements_check.TOCHKA_B)

    @allure.step("Отображаение блока маршрута")
    def wait_point_exist(self):
        return self.find_long_element(Elements_check.ROUTE_CARD)

    @allure.step("Заполнение формы карты Откуда и Куда одинаковыми данными")
    def fill_same_data_route_to(self):
        self.input_text(Elements_check.ADDRESS_CONTAINER_TO, Data.ADDRESS_1[0])
