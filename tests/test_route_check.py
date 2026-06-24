import pytest
import allure


class TestRoutePage:

    @allure.title('Отрисовка блока с выбором маршрута')
    @allure.description('Проверить: при вводе двух адресов отображается начало и конец марщшрута')
    def test_route_page(self, driver, fill_data_route, route_page):
     
        point_a = route_page.wait_point_exist_a()
        point_b = route_page.wait_point_exist_b()

        assert point_a.is_displayed()
        assert point_b.is_displayed()


        