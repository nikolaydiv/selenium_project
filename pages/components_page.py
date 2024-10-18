import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from base.base_class import Base


class ComponentsPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    pc_components = "//li[@id='bx_1847241719_13524']"
    title = "//h1[@id='pagetitle']"

    # Getters

    def get_pc_components(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.pc_components)))

    def get_title(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.title)))

    # Actions

    def click_pc_components(self):
        self.get_pc_components().click()
        print("Click pc components")

    # Methods

    def choose_pc_components(self):
        self.get_current_url()
        self.assert_url('https://shop.kz/catalog/komplektuyushchie/')
        self.assert_word(self.get_title(), 'Комплектующие')
        self.click_pc_components()
