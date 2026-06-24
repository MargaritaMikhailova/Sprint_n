import allure

from locators import Elements_check, Buttons
from pages.base_page import BasePage


class PrepareOrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Выбор передвижение на машине")
    def click_choose_car(self):
        element = self.find_clickable_element(Buttons.CAR_BUTTON)
        element.click()
        return element

    @allure.step("Выбор передвижение на такси")
    def click_choose_taxi(self):
        element = self.find_clickable_element(Buttons.TAXI_BUTTON)
        element.click()
        return element

    @allure.step("Выбор передвижение на велосипеде")
    def click_choose_bike(self):
        element = self.find_clickable_element(Buttons.BIKE_BUTTON)
        element.click()
        return element

    @allure.step("Выбор передвижение на самокате")
    def click_choose_scooter(self):
        element = self.find_clickable_element(Buttons.SCOOTER_BUTTON)
        element.click()
        return element

    @allure.step("Выбор передвижение пешком")
    def click_choose_walk(self):
        element = self.find_clickable_element(Buttons.WALK_BUTTON)
        element.click()
        return element

    @allure.step("Выбор передвижение каршерингом")
    def click_choose_car_rent(self):
        element = self.find_clickable_element(Buttons.DRIVE_BUTTON)
        element.click()
        return element

    @allure.step("Выбор маршрута Оптимальный")
    def click_choose_route_opti(self):
        self.click(Buttons.OPTIMAL_BUTTON)

    @allure.step("Выбор маршрута Быстрый")
    def click_choose_route_fast(self):
        self.click(Buttons.FASTER_BUTTON)

    @allure.step("Выбор маршрута Свой")
    def click_choose_route_myself(self):
        self.click(Buttons.MYSELF_BUTTON)

    @allure.step("Нажать кнопку вызвать такси для типа Такси")
    def click_get_order_taxi(self):
        element = self.find_clickable_element(Buttons.GET_ORDER_TAXI)
        element.click()
        return element

    @allure.step("Нажать кнопку забронировать для типа Драйв")
    def click_rent_car_drive(self):
        element = self.find_clickable_element(Buttons.RENT_CAR_TAXI)
        element.click()
        return element
