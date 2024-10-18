import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from base.base_class import Base


class WishlistPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    title = "//h1[@id='pagetitle']"
    product_name_wishlist_1 = "(//div[@class='g-i-tile-i-title'])[1]"
    product_price_wishlist_1 = "(//div[@class='g-i-tile-i-price']//b)[1]"
    delete_from_wishlist_1 = "(//li[@class='g-i-tile-i-delete'])[1]"
    delete_from_wishlist_2 = "(//li[@class='g-i-tile-i-delete'])[2]"
    delete_from_wishlist_3 = "(//li[@class='g-i-tile-i-delete'])[3]"

    # Getters

    def get_title(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.title)))

    def get_product_name_wishlist_1(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.product_name_wishlist_1)))

    def get_product_price_wishlist_1(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.product_price_wishlist_1)))

    def get_delete_from_wishlist_1(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.delete_from_wishlist_1)))

    def get_delete_from_wishlist_2(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.delete_from_wishlist_2)))

    def get_delete_from_wishlist_3(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.delete_from_wishlist_3)))

    # Actions

    def click_delete_from_wishlist_1(self):
        self.get_delete_from_wishlist_1().click()
        print("Click delete from wishlist")

    def click_delete_from_wishlist_2(self):
        self.get_delete_from_wishlist_2().click()
        print("Click delete from wishlist")

    def click_delete_from_wishlist_3(self):
        self.get_delete_from_wishlist_3().click()
        print("Click delete from wishlist")

    # Methods

    def wishlist_check(self, expected_items):
        self.get_current_url()
        self.assert_url('https://shop.kz/personal/wishlist/')
        self.assert_word(self.get_title(), 'Мой список желаний')

        # цикл для сравнения нескольких товаров
        for index, expected_item in enumerate(expected_items, start=1):
            product_name_locator = f"(//div[@class='g-i-tile-i-title'])[{index}]"
            product_price_locator = f"(//div[@class='g-i-tile-i-price']//b)[{index}]"

            product_name_in_cart = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, product_name_locator))).text
            print(product_name_in_cart)
            product_price_in_cart = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, product_price_locator))).text
            print(product_price_in_cart)

            assert product_name_in_cart == expected_item['name']
            print(f'Название товара {index} совпадает. Ожидается: {expected_item["name"]}, имеем: {product_name_in_cart}')
            assert product_price_in_cart == expected_item['price']
            print(f'Цена товара {index} совпадает. Ожидается: {expected_item["price"]}, имеем: {product_price_in_cart}')

        self.get_screenshot_wishlist()

    def clear_wishlist(self):
        self.click_delete_from_wishlist_1()
        self.click_delete_from_wishlist_2()
        self.click_delete_from_wishlist_3()
        time.sleep(3)  # чтобы виш итемы успели убраться
        self.get_screenshot_wishlist()
