import allure

from locators import Elements_check, Buttons
from pages.base_page import BasePage


class GetOrderTaxiPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Выбор машины Рабочий")
    def choose_work_car(self):
        element = self.find_clickable_element(Buttons.WORK_CAR_BUTTON)
        element.click()
        return element

    @allure.step("Выбор машины Сонный")
    def choose_son_car(self):
        element = self.find_clickable_element(Buttons.SON_CAR_BUTTON)
        element.click()
        return element

    @allure.step("Выбор машины Отпускной")
    def choose_vacation_car(self):
        element = self.find_clickable_element(Buttons.VACATION_CAR_BUTTON)
        element.click()
        return element

    @allure.step("Выбор машины Разговорчивый")
    def choose_talk_car(self):
        element = self.find_clickable_element(Buttons.TALK_CAR_BUTTON)
        element.click()
        return element

    @allure.step("Выбор машины Гламурный")
    def choose_glamour_car(self):
        element = self.find_clickable_element(Buttons.GLAMOUR_CAR_BUTTON)
        element.click()
        return element

    @allure.step("Выбор машины Утешительный")
    def choose_comfort_car(self):
        element = self.find_clickable_element(Buttons.COMFORT_CAR_BUTTON)
        element.click()
        return element

    @allure.step("Ожидание загрузки окна с тарифами")
    def choose_tariff(self):
        return self.find_long_element(Elements_check.CHOOSE_TARIFF)

    @allure.step("Ожидание загрузки окна с тарифами")
    def check_choose_tariff(self):
        return self.is_element_visible(Elements_check.CHOOSE_TARIFF)

    @allure.step("Ожидание загрузки окна Телефон")
    def wait_tab_phone(self):
        self.find_long_element(Elements_check.PHONE_NUMBER_TAB)
        return self.is_element_visible(Elements_check.PHONE_NUMBER_TAB)

    @allure.step("Ожидание загрузки окна Способ оплаты")
    def wait_tab_change_payment(self):
        return self.is_element_visible(Elements_check.PAYMENT_METHOD_TAB)

    @allure.step("Ожидание загрузки окна Комментарию водителю")
    def wait_tab_comment(self):
        self.find_element(Elements_check.COMMENT_TAB)
        return self.is_element_visible(Elements_check.COMMENT_TAB)

    @allure.step("Ожидание загрузки окна Требованию к заказу")
    def wait_tab_requirements(self):
        self.click_with_scroll(Elements_check.ORDER_REQUIREMENTS_TAB)
        return self.is_element_visible(Elements_check.ORDER_REQUIREMENTS_TAB)

    @allure.step("Наведение на иконку i")
    def hover_icon(self):
        self.hover(Elements_check.ICON_ICON)
        return self.is_element_visible(Elements_check.TARIFF_TOOLTIP)

    @allure.step("Нажать на кнопку Ввести номер и заказать")
    def fill_number_and_create_order(self):
        element = self.find_clickable_element(Buttons.CREATE_ORDER_BUTTON)
        element.click()
        return element

    @allure.step("Проверить активный тариф")
    def get_active_tariff(self):
        return self.find_long_element(Elements_check.ACTIVE_TARIFF)

    @allure.step("Получить название активного тарифа")
    def get_active_tariff_name(self):
        return self.get_text(Elements_check.ACTIVE_TARIFF)

    @allure.step("Получить описание тарифа")
    def get_tariff_description(self):
        self.hover(Elements_check.ICON_ICON)
        tooltip = self.get_displayed_element(Elements_check.TARIFF_TOOLTIP)
        return tooltip.text

    def move_away_from_icon(self):
        self.hover(Elements_check.CHOOSE_TARIFF)

    @allure.step("Отображаение кнопки Ввести номер и заказать")
    def check_exist_create_order(self):
        return self.is_element_visible(Buttons.CREATE_ORDER_BUTTON)

    @allure.step("Кликнуть на окно Требованию к заказу")
    def click_tab_requirements(self):
        self.click(Elements_check.ORDER_REQUIREMENTS_TAB)
        self.scroll_to_element(Elements_check.TAB_REQUIREMENT)

    @allure.step("Найти чекбокс и нажать Столик для ноутбука")
    def wait_and_click_checkboks_table(self):
        self.find_long_element(Elements_check.NOTEPAD_TAB)
        self.click(Elements_check.NOTEPAD_CHECKBOKS)

    @allure.step("Отображение окно ожиданиня машины")
    def wait_tab_taxi(self):
        return self.is_element_visible(Elements_check.WAIT_CAR_TAB)

    @allure.step("Отображение кнопки Детали")
    def wait_tab_detils(self):
        return self.is_element_visible(Buttons.DETAILS_BUTTON)

    @allure.step("Отображение кнопки Отменить")
    def wait_tab_cancel(self):
        return self.is_element_visible(Buttons.CANCEL_BUTTON)

    @allure.step("Отображение информации о водители")
    def wait_tab_data_driver(self):
        return self.is_element_visible(Elements_check.DATA_NUMBER)

    @allure.step("Нажать на кнопку Детали")
    def click_details_button(self):
        self.click(Buttons.DETAILS_BUTTON)
        return self.is_element_visible(Elements_check.AMOUNT_TAXI_TAB)

    @allure.step("Нажать на кнопку Отменить")
    def click_cancel_button(self):
        self.click(Buttons.CANCEL_BUTTON)

    @allure.step("Отображение номера машины")
    def check_number_car(self):
        return self.is_element_visible(Elements_check.NUMBER_CAR).text

    @allure.step("Ждать окно с таймером прибытия машины")
    def wait_car_timer_tab(self):
        return self.is_element_visible(Elements_check.WAIT_TIMER_TAXI_TAB)

    @allure.step("Отображение n мин. и приедет")
    def check_wait_taxi(self):
        return self.wait_car_timer_tab().text

    @allure.step("Отображения табы информации о заказе такси")
    def check_tab_infromation(self):
        return self.find_element(Elements_check.DESCRIBE_TAXI_TAB)

    @allure.step("Отображения информации о стоимости поездки")
    def check_amount_information_taxi(self):
        return self.is_element_visible(Elements_check.AMOUNT_TAXI_TAB).text

    @allure.step("Отображения информации о типе способе оплаты")
    def check_type_payment_information_taxi(self):
        return self.is_element_visible(Elements_check.TYPE_PAYMENT).text

    @allure.step("Отображения табы с деталями о заказе")
    def check_tab_infromation_details(self):
        return self.find_element(Elements_check.DESCRIBE_DETAILS_TAB)

    @allure.step("Отображение название окна Поиск машины")
    def wait_tab_find_car(self):
        return self.is_element_visible(Elements_check.FIND_CAR_TAB)

    @allure.step("Загрузка окна ожидания машины")
    def wait_tab_taxi_prepare(self):
        return self.find_long_element(Elements_check.WAIT_CAR_TAB)

    @allure.step("Дождаться, что машина найдена")
    def wait_car_found(self):
        return self.wait_for_displayed_element(Elements_check.WAIT_TIMER_TAXI_TAB)
