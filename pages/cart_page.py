import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from base.base_class import Base


class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    title = "//h1[@id='pagetitle']"
    product_name_cart_1 = "(//div[@class='cart-bill-name'])[1]"
    product_price_cart_1 = "(//strong[@class='item__price item__price--cart'])[1]"
    final_price_cart = "//div[@class='basket-items-summary__summ']"

    # Getters

    def get_title(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.title)))

    def get_product_name_cart_1(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.product_name_cart_1)))

    def get_product_price_cart_1(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.product_price_cart_1)))

    def get_final_price_cart(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.final_price_cart)))

    # Methods

    def cart_check_one_product(self, expected_name, expected_price):  # сверка названия и цены одного товара на странице товаров и на странице корзины
        self.get_current_url()
        self.assert_url('https://shop.kz/personal/basket/')
        self.assert_word(self.get_title(), 'Моя корзина')

        product_name_in_cart = self.get_product_name_cart_1().text
        product_price_in_cart = self.get_product_price_cart_1().text
        final_price_in_cart = self.get_final_price_cart().text

        assert (product_name_in_cart == expected_name)
        print(f'Название товара совпадает. Ожидается: {expected_name}, имеем: {product_name_in_cart}')
        assert (product_price_in_cart == expected_price)
        print(f'Цена товара совпадает. Ожидается: {expected_price}, имеем: {product_price_in_cart}')
        assert (product_price_in_cart == final_price_in_cart)
        print(f'Итоговая цена совпадает. Ожидается: {expected_price}, имеем: {final_price_in_cart}')

        self.get_screenshot_buy_one_product()

    def cart_check_several_products(self, expected_items):  # сверка названий и цен нес-х товаров на странице товаров и на странице корзины
        self.get_current_url()
        self.assert_url('https://shop.kz/personal/basket/')
        self.assert_word(self.get_title(), 'Моя корзина')
        sum_final_price_int = 0

        def get_final_price_cart(): return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.final_price_cart)))

        # цикл для сравнения нескольких товаров
        for index, expected_item in enumerate(expected_items, start=1):
            product_name_locator = f"(//div[@class='cart-bill-name'])[{index}]"
            product_price_locator = f"(//strong[@class='item__price item__price--cart'])[{index}]"

            product_name_in_cart = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, product_name_locator))).text
            product_price_in_cart = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, product_price_locator))).text
            # суммирование цен добавленных товаров, убираем знак валюты для сложения и преобразуем в int
            sum_final_price_int += int(product_price_in_cart.replace(" ₸", "").replace(" ", ""))

            assert product_name_in_cart == expected_item['name']
            print(f'Название товара {index} совпадает. Ожидается: {expected_item["name"]}, имеем: {product_name_in_cart}')
            assert product_price_in_cart == expected_item['price']
            print(f'Цена товара {index} совпадает. Ожидается: {expected_item["price"]}, имеем: {product_price_in_cart}')

        # возвращаем знак валюты к сумме товаров
        sum_final_price = f"{sum_final_price_int:,}".replace(",", " ") + " ₸"
        # преобразуем сумму товаров в str для assert
        assert str(sum_final_price) == get_final_price_cart().text
        print(f"Общая стоимость в корзине: {get_final_price_cart().text} совпадает с суммой всех товаров: {sum_final_price}")
        self.get_screenshot_buy_several_products()
