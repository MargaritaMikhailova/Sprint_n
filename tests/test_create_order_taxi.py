import pytest
import allure

from data import Data


class TestGetOrderTaxiPage:

    @allure.title('Заказ тарифа Такси')
    @allure.description('Проверить: открывается форма заказа со всеми 6 тарифами по ТЗ, один из них активный')
    def test_check_available_tariffs(self, driver, fill_type_route, get_order_taxi_page):
        tariff_form = get_order_taxi_page.check_choose_tariff()
        assert tariff_form.is_displayed()

        work_car = get_order_taxi_page.choose_work_car()
        son_car = get_order_taxi_page.choose_son_car()
        vacation_car = get_order_taxi_page.choose_vacation_car()
        talk_car = get_order_taxi_page.choose_talk_car()
        comfort_car = get_order_taxi_page.choose_comfort_car()
        glamour_car = get_order_taxi_page.choose_glamour_car()

        assert work_car.is_displayed()
        assert son_car.is_displayed()
        assert vacation_car.is_displayed()
        assert talk_car.is_displayed()
        assert comfort_car.is_displayed()
        assert glamour_car.is_displayed()

        active_tariff = get_order_taxi_page.get_active_tariff()
        assert active_tariff.is_displayed()
        assert work_car.text == Data.TARIFFS[0]

    @pytest.mark.xfail(reason="Баг на описание тарифа Сонный и Разговорчивый")
    @allure.title('Заказ тарифа Такси')
    @allure.description('Проверить: при наведении на иконку i в правом верхнем углу каждого тарифа отображается всплывающее окно с описанием тарифа')
    def test_check_describe_tariff(self, driver, fill_type_route, get_order_taxi_page):
        get_order_taxi_page.check_choose_tariff()

        get_order_taxi_page.choose_work_car()
        assert Data.WORK_CAR[0] in get_order_taxi_page.get_tariff_description()

        get_order_taxi_page.choose_vacation_car()
        get_order_taxi_page.move_away_from_icon()
        assert Data.VACATION_CAR[0] in get_order_taxi_page.get_tariff_description()

        get_order_taxi_page.choose_comfort_car()
        get_order_taxi_page.move_away_from_icon()
        assert Data.COMFORT_CAR[0] in get_order_taxi_page.get_tariff_description()

        get_order_taxi_page.choose_glamour_car()
        get_order_taxi_page.move_away_from_icon()
        assert Data.GLAMOUR_CAR[0] in get_order_taxi_page.get_tariff_description()

        get_order_taxi_page.choose_son_car()
        get_order_taxi_page.move_away_from_icon()
        assert Data.SON_CAR[0] in get_order_taxi_page.get_tariff_description()

        get_order_taxi_page.choose_talk_car()
        get_order_taxi_page.move_away_from_icon()
        assert Data.TALK_CAR[0] in get_order_taxi_page.get_tariff_description()

    @allure.title('Заказ тарифа Такси')
    @allure.description('Проверить: под тарифами отображается блок с полями Телефон, Способ оплаты, Комментарий водителю, Требования к заказу Заказ тарифа Такси')
    def test_check_block_addiotional_tariffs(self, driver, fill_type_route, get_order_taxi_page):
        get_order_taxi_page.check_choose_tariff()

        tariffs = [
            get_order_taxi_page.choose_work_car,
            get_order_taxi_page.choose_son_car,
            get_order_taxi_page.choose_talk_car,
            get_order_taxi_page.choose_vacation_car,
            get_order_taxi_page.choose_glamour_car,
            get_order_taxi_page.choose_comfort_car
        ]

        for choise in tariffs:
            choise()
            assert get_order_taxi_page.wait_tab_phone().is_displayed()
            assert get_order_taxi_page.wait_tab_change_payment().is_displayed()
            assert get_order_taxi_page.wait_tab_comment().is_displayed()
            assert get_order_taxi_page.wait_tab_requirements().is_displayed()
            assert get_order_taxi_page.check_exist_create_order().is_displayed()

    @allure.title('Заказ тарифа Такси')
    @allure.description('Проверить: окно ожидания машины')
    def test_check_wait_taxi_tab(self, driver, fill_type_route, get_order_taxi_page):
        get_order_taxi_page.click_tab_requirements()
        get_order_taxi_page.wait_and_click_checkboks_table()
        get_order_taxi_page.fill_number_and_create_order()

        assert get_order_taxi_page.wait_tab_taxi().is_displayed()
        assert get_order_taxi_page.wait_tab_detils().is_displayed()
        assert get_order_taxi_page.wait_tab_cancel().is_displayed()
        assert get_order_taxi_page.wait_tab_find_car().is_displayed()

    @allure.title('Заказ тарифа Такси')
    @allure.description('Проверить: окно совершенного заказа')
    def test_check_ready_order_taxi(self, driver, fill_type_route, get_order_taxi_page):
        get_order_taxi_page.click_tab_requirements()
        get_order_taxi_page.fill_number_and_create_order()
        get_order_taxi_page.wait_tab_taxi_prepare()
        get_order_taxi_page.wait_car_found()
        get_order_taxi_page.wait_car_timer_tab()

        assert Data.WAIT_TAXI[0] in get_order_taxi_page.check_wait_taxi()
        assert get_order_taxi_page.check_number_car()

        assert get_order_taxi_page.wait_tab_data_driver().is_displayed()
        assert get_order_taxi_page.wait_tab_detils().is_displayed()
        assert get_order_taxi_page.wait_tab_cancel().is_displayed()

    @allure.title('Заказ тарифа Такси')
    @allure.description('Проверить: окно Детали')
    def test_check_amount_taxi(self, driver, fill_type_route, get_order_taxi_page, selector_page):
        amount_route = selector_page.check_amount_block().text

        get_order_taxi_page.click_tab_requirements()
        get_order_taxi_page.fill_number_and_create_order()
        get_order_taxi_page.wait_tab_taxi_prepare()
        get_order_taxi_page.wait_car_found()
        get_order_taxi_page.wait_car_timer_tab()

        assert get_order_taxi_page.wait_tab_detils().is_displayed()
        assert get_order_taxi_page.wait_tab_cancel().is_displayed()

        get_order_taxi_page.click_details_button()
        assert get_order_taxi_page.check_type_payment_information_taxi()
        total_amount = get_order_taxi_page.check_amount_information_taxi()

        route_price = amount_route.split("~")[-1].strip()
        assert route_price.split()[0] in total_amount

    @allure.title('Заказ тарифа Такси')
    @allure.description('Проверить: окно Детали')
    def test_check_cancel_taxi(self, driver, fill_type_route, get_order_taxi_page, route_page):
        get_order_taxi_page.click_tab_requirements()
        get_order_taxi_page.fill_number_and_create_order()
        get_order_taxi_page.wait_tab_taxi_prepare()
        get_order_taxi_page.wait_car_found()
        get_order_taxi_page.wait_car_timer_tab()

        assert get_order_taxi_page.wait_tab_cancel().is_displayed()

        get_order_taxi_page.click_cancel_button()
        assert route_page.wait_for_load_page().is_displayed()
