import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from base.base_class import Base


class MainPage(Base):
    url = "https://www.shop.kz/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    catalog_button = "//div[@id='catalog_menu_XEVOpk']"
    pop_up_close = "//span[@id='popup-1094-close']"
    choose_city = "//div[@class='base-ui-button base-ui-button_grey']"
    default_city = "//span[@class='city-default-list__city-active city-default-list__city-bubble']"
    close_button = "//i[@class='modal-popup_header-close-icon']"
    pc_components_category = "//span[text()='Комплектующие']"
    smartphones_category = "//a[@id='bx_651765591_1620520']"

    # Getters

    def get_catalog_button(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.catalog_button)))

    def get_pop_up_close(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.pop_up_close)))

    def get_choose_city(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.choose_city)))

    def get_default_city(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.default_city)))

    def get_close_button(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.close_button)))

    def get_pc_components_category(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.pc_components_category)))

    def get_smartphones_category(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.smartphones_category)))

    # Actions

    def click_pop_up_close(self):
        self.get_pop_up_close().click()
        print("Click pop up close")

    def click_choose_city(self):
        self.get_choose_city().click()
        print("Click city confirm")

    def click_default_city(self):
        self.get_default_city().click()
        print("Click default city")

    def close_city_window(self):
        self.get_close_button().click()
        print("Click close button")

    def click_catalog_button(self):
        self.get_catalog_button().click()
        print("Click catalog button")

    def click_pc_components_category(self):
        self.get_pc_components_category().click()
        print("Click pc components category")

    def click_smartphones_category(self):
        self.get_smartphones_category().click()
        print("Click smartphones category")

    # Methods

    def enter_page(self):
        self.driver.get(self.url)
        self.get_current_url()
        self.assert_url("https://shop.kz/")
        time.sleep(5)  # waiting for pop up to appear
        self.click_pop_up_close()
        self.click_choose_city()
        self.click_default_city()
        self.close_city_window()

    def select_catalog(self):
        self.click_catalog_button()
        self.click_pc_components_category()

    def select_smartphones(self):
        self.click_smartphones_category()
