import pytest

from selenium import webdriver

from data import Urls
from pages.route_page import RoutePage
from pages.selector_page import SelectorPage
from pages.prepare_order_page import PrepareOrderPage
from pages.get_order_taxi import GetOrderTaxiPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(Urls.MAIN_PAGE)

    yield driver

    driver.quit()

@pytest.fixture
def route_page(driver):
    return RoutePage(driver)

@pytest.fixture
def selector_page(driver):
    return SelectorPage(driver)

@pytest.fixture
def fill_data_route(route_page):
    route_page.wait_for_load_page()
    route_page.wait_load_menu_page()
    route_page.fill_data_route_from()
    route_page.fill_data_route_to()
    return route_page

@pytest.fixture
def fill_same_address_route(route_page):
    route_page.wait_for_load_page()
    route_page.wait_load_menu_page()
    route_page.fill_data_route_from()
    route_page.fill_same_data_route_to()
    return route_page

@pytest.fixture
def prepare_order_page(driver):
    return PrepareOrderPage(driver)

@pytest.fixture
def get_order_taxi_page(driver):
    return GetOrderTaxiPage(driver)

@pytest.fixture
def fill_type_route(fill_data_route, prepare_order_page):
    prepare_order_page.click_choose_route_fast()
    prepare_order_page.click_get_order_taxi()
    return prepare_order_page
