import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from base.base_class import Base


class ComparisonPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    title = "//h1[@id='pagetitle']"
    # compare_product_name_1 = "(//div[@class='bs5'])[1]"  # нормальные локаторы
    # compare_product_name_2 = "(//div[@class='bs5'])[2]"
    compare_product_name_1 = "(//a[contains(text(), 'Samsung')])[1]"  # костыльный локатор, т.к. в нормальный входит артикул товара
    compare_product_name_2 = "(//a[contains(text(), 'Samsung')])[2]"  # если браузер не в полноэкранном режиме, то можно с нормальным локатором, т.к. артикул не отображается
    compare_product_price_1 = "(//div[@class='bt8 compare_property'])[5]"  # беру строку "Цена в интернет-магазине"
    compare_product_price_2 = "(//div[@class='bt8 compare_property'])[6]"
    delete_compare_product_1 = "(//div[@class='bs1'])[1]"
    delete_compare_product_2 = "(//div[@class='bs1'])[2]"
    empty_comparison_title = "//div[@class='bx-content col-xs-12']"

    # Getters

    def get_title(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.title)))

    def get_compare_product_name_1(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.compare_product_name_1)))

    def get_compare_product_name_2(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.compare_product_name_2)))

    def get_compare_product_price_1(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.compare_product_price_1)))

    def get_compare_product_price_2(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.compare_product_price_2)))

    def get_delete_compare_product_1(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.delete_compare_product_1)))

    def get_delete_compare_product_2(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.delete_compare_product_2)))

    def get_empty_comparison_title(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.empty_comparison_title)))

    # Actions

    # Methods

    def check_comparison(self):
        self.get_current_url()
        self.assert_url("https://shop.kz/catalog/compare.php")
        self.assert_word(self.get_title(), "Сравнение товаров")
        self.get_screenshot_compare_products()

    def delete_comparing_products(self):
        self.get_delete_compare_product_1().click()
        print("Click delete compare product 1")
        self.get_delete_compare_product_2().click()
        print("Click delete compare product 2")
        time.sleep(1)  # чтобы товары успели удалиться
        self.assert_word(self.get_empty_comparison_title(), "Список сравнения пуст")
        self.get_screenshot_compare_products()
