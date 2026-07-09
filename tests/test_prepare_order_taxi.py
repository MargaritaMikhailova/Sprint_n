import pytest
import allure

from data import Data


class TestPrepareOrderPage:


    @allure.title('Подготовка к заказу такси')
    @allure.description('Проверить: при переключении между видами маршрута (Оптимальный\Быстрый) происходит смена активного таба и пересчет времени и стоимости маршрута')
    def test_check_change_option(self, driver, fill_data_route, prepare_order_page, selector_page):
        prepare_order_page.click_choose_route_opti()

        amount_route = selector_page.check_amount_block()
        time_route = selector_page.check_time_block()

        assert amount_route.is_displayed()
        assert amount_route.text == Data.AMOUNT_ROUTE
        assert time_route.is_displayed()
        assert time_route.text == Data.TIME_ROUTE

        prepare_order_page.click_choose_route_fast()

        amount_route = selector_page.check_amount_block()
        time_route = selector_page.check_time_block()
   
        assert amount_route.is_displayed()
        assert amount_route.text == Data.TAXI_AMOUNT_ROUTE
        assert time_route.is_displayed()
        assert time_route.text == Data.TAXI_TIME_ROUTE

    @allure.title('Подготовка к заказу такси')
    @allure.description('Проверить: при переключении на вид маршрута Свой происходит смена активного таба и становятся активны типы передвижения (Машина, Пешком, Такси, Велосипед, Самокат, Драйв)')
    def test_check_active_option_myself(self, driver, fill_data_route, prepare_order_page):
        prepare_order_page.click_choose_route_myself()

        car_button = prepare_order_page.click_choose_car()
        walk_button = prepare_order_page.click_choose_walk()
        taxi_button = prepare_order_page.click_choose_taxi()
        bike_button = prepare_order_page.click_choose_bike()
        scooter_button = prepare_order_page.click_choose_scooter()
        drive_button = prepare_order_page.click_choose_car_rent()

        assert car_button.is_displayed()
        assert walk_button.is_displayed()
        assert taxi_button.is_displayed()
        assert bike_button.is_displayed()
        assert scooter_button.is_displayed()
        assert drive_button.is_displayed()

    @allure.title('Подготовка к заказу такси')
    @allure.description('Проверить: при выборе вида маршрута Быстрый активна кнопка Вызвать такси')
    def test_check_button_get_taxi_active(self, driver, fill_data_route, prepare_order_page):
        prepare_order_page.click_choose_route_fast()

        taxi_button_active = prepare_order_page.click_get_order_taxi()
        assert taxi_button_active.is_displayed()
        assert taxi_button_active.text == Data.GET_ORDER_TAXI_BUTTON
      
    @allure.title('Подготовка к заказу такси')
    @allure.description('Проверить: при выборе вида маршрута Свой, типа передвижения Драйв активна кнопка Забронировать')
    def test_check_button_get_rent_car_active(self, driver, fill_data_route, prepare_order_page):
        prepare_order_page.click_choose_route_myself()
        prepare_order_page.click_choose_car_rent()

        car_button_active = prepare_order_page.click_rent_car_drive()
        assert car_button_active.is_displayed()
        assert car_button_active.text == Data.RENT_CAR_BUTTON
      