import pytest
import allure

from data import Data


class TestSelectorPage:

    @allure.title('Отрисовка маршрута')
    @allure.description('Проверить: на карте отображаются блок с выбором маршрута')
    def test_check_selector_route_type(self, driver, fill_data_route, selector_page):
        select_route = selector_page.wait_selector_menu_page()

        assert select_route.is_displayed()

    @allure.title('Отрисовка маршрута')
    @allure.description('Проверить: при вводе одинакового адреса в поля "Откуда" и "Куда" под выбором адресов отображается блок с выбором маршрута с текстом "Авто Бесплатно В пути 0 мин."')
    def test_same_address_selector_route_type(self, driver, fill_same_address_route, selector_page):
        selector_page.wait_selector_menu_page()

        amount_route = selector_page.check_amount_block()
        time_route = selector_page.check_time_block()

        assert amount_route.is_displayed()
        assert amount_route.text == Data.FREE_AUTO
        assert time_route.is_displayed()
        assert time_route.text == Data.FREE_AUTO_TIME

