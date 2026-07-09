from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.long_wait = WebDriverWait(driver, 60)
        self.actions = ActionChains(driver)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_long_element(self, locator):
        return self.long_wait.until(EC.presence_of_element_located(locator))

    def find_clickable_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        element = self.find_clickable_element(locator)
        element.click()

    def click_with_scroll(self, locator):
        element = self.find_clickable_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)

    def input_text(self, locator, text):
        element = self.find_clickable_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find_element(locator).text

    def is_element_visible(self, locator):
        return self.long_wait.until(EC.visibility_of_element_located(locator))

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def wait_for_url_contains(self, data):
        return self.long_wait.until(EC.url_contains(data))

    def switch_to_new_window(self):
        self.long_wait.until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def click_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def get_current_url_page(self) -> str:
        return self.driver.current_url

    def upload_file(self, locator, file_path):
        upload_input = self.find_element(locator)
        upload_input.send_keys(str(file_path))


    def hover(self, locator):
        element = self.find_element(locator)
        action = ActionChains(self.driver).move_to_element(element)
        action.perform()

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def get_displayed_element(self, locator):
        for element in self.find_elements(locator):
            if element.is_displayed():
                return element

    def wait_for_displayed_element(self, locator):
        def element_is_displayed(driver):
            for element in driver.find_elements(*locator):
                if element.is_displayed():
                    return element
            return False
        return self.long_wait.until(element_is_displayed)

