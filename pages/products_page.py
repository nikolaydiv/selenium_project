import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from base.base_class import Base


class ProductsPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    min_price = "//input[@id='filter_02_P7_MIN']"
    max_price = "//input[@id='filter_02_P7_MAX']"
    show_all_vendors_videocards = "(//button[@class='btn btn-link bx-filter-toggle-expand'])[5]"
    palit_checkbox = "//label[@for='filter_02_216_2361444709']"
    nvidia_checkbox = "//label[@for='filter_02_203_3677994516']"
    show_all_series_videocards = "(//button[@class='btn btn-link bx-filter-toggle-expand'])[7]"
    series_videocards_1 = "//label[@for='filter_02_2353_59403655']"
    series_videocards_2 = "//label[@for='filter_02_2353_973720173']"
    show_all_models_videocards = "(//button[@class='btn btn-link bx-filter-toggle-expand'])[8]"
    model_videocard_1 = "//label[@for='filter_02_19450_503051091']"
    model_videocard_2 = "//label[@for='filter_02_19450_2403339277']"
    model_videocard_3 = "//label[@for='filter_02_19450_1258737888']"
    show_filtered_button = "//a[@class='btn btn-xs btn-primary']"
    buy_product = "(//a[@class='bx_bt_button bx_medium'])[1]"
    product_name_1 = "(//h4[@class='bx_catalog_item_title_text'])[1]"
    product_price_1 = "(//span[@class='current_price'])[1]"
    product_name_2 = "(//h4[@class='bx_catalog_item_title_text'])[2]"
    product_price_2 = "(//span[@class='current_price'])[2]"
    product_name_3 = "(//h4[@class='bx_catalog_item_title_text'])[3]"
    product_price_3 = "(//span[@class='current_price'])[3]"
    cart = "//div[@id='bx_basketFKauiI']"
    show_all_vendors_smartphones = "(//button[@class='btn btn-link bx-filter-toggle-expand'])[4]"
    samsung_checkbox = "//input[@id='filter_02_223_3828447656']"
    smartphones_storage_filter = "(//button[@class='btn btn-link bx-filter-toggle-expand'])[12]"
    storage_256 = "//input[@id='filter_02_386_2742115348']"
    add_to_comparison_1 = "//a[@id='bx_2862482274_1623367_compare_link']"
    add_to_comparison_2 = "//a[@id='bx_2862482274_1623298_compare_link']"
    comparison = "//li[@id='comparison-header']"
    add_to_wishlist_1 = "(//a[@name='towishlist'])[1]"
    add_to_wishlist_2 = "(//a[@name='towishlist'])[2]"
    add_to_wishlist_3 = "(//a[@name='towishlist'])[3]"
    wishlist = "//li[@id='wishlist-header']"

    # Getters

    def get_min_price(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.min_price)))

    def get_max_price(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.max_price)))

    def get_show_all_vendors_videocards(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.show_all_vendors_videocards)))

    def get_palit_checkbox(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.palit_checkbox)))

    def get_nvidia_checkbox(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.nvidia_checkbox)))

    def get_show_all_series_videocards(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.show_all_series_videocards)))

    def get_series_videocards_1(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.series_videocards_1)))

    def get_series_videocards_2(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.series_videocards_2)))

    def get_show_all_models_videocards(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.show_all_models_videocards)))

    def get_model_videocard_1(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.model_videocard_1)))

    def get_model_videocard_2(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.model_videocard_2)))

    def get_model_videocard_3(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.model_videocard_3)))

    def get_show_filtered_button(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.show_filtered_button)))

    def get_buy_product(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.buy_product)))

    def get_product_name_1(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.product_name_1)))

    def get_product_price_1(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.product_price_1)))

    def get_product_name_2(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.product_name_2)))

    def get_product_price_2(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.product_price_2)))

    def get_product_name_3(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.product_name_3)))

    def get_product_price_3(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.product_price_3)))

    def get_cart(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_show_all_vendors_smartphones(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.show_all_vendors_smartphones)))

    def get_samsung_checkbox(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.samsung_checkbox)))

    def get_smartphones_storage_filter(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.smartphones_storage_filter)))

    def get_storage_256(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.storage_256)))

    def get_add_to_comparison_1(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.add_to_comparison_1)))

    def get_add_to_comparison_2(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.add_to_comparison_2)))

    def get_comparison(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.comparison)))

    def get_add_to_wishlist_1(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.add_to_wishlist_1)))

    def get_add_to_wishlist_2(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.add_to_wishlist_2)))

    def get_add_to_wishlist_3(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.add_to_wishlist_3)))

    def get_wishlist(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.wishlist)))

    # Actions

    def input_min_price(self):
        self.get_min_price().send_keys("200000")
        print("Input min price")

    def input_max_price(self):
        self.get_max_price().send_keys("1000000")
        print("Input max price")

    def click_show_all_vendors_videocards(self):
        self.get_show_all_vendors_videocards().click()
        print("Click show all vendors videocards")

    def click_palit_checkbox(self):
        self.get_palit_checkbox().click()
        print("Click palit checkbox")

    def click_nvidia_checkbox(self):
        self.get_nvidia_checkbox().click()
        print("Click nvidia checkbox")

    def click_show_all_series_videocards(self):
        self.get_show_all_series_videocards().click()
        print("Click show all series videocards")

    def click_series_videocards_1(self):
        self.get_series_videocards_1().click()
        print("Click series 1 videocards")

    def click_series_videocards_2(self):
        self.get_series_videocards_2().click()
        print("Click series videocards 2")

    def click_show_all_models_videocards(self):
        self.get_show_all_models_videocards().click()
        print("Click show all models videocards")

    def click_model_videocard_1(self):
        self.get_model_videocard_1().click()
        print("Click model videocard 1")

    def click_model_videocard_2(self):
        self.get_model_videocard_2().click()
        print("Click model videocard 2")

    def click_model_videocard_3(self):
        self.get_model_videocard_3().click()
        print("Click model videocard 3")

    def click_show_filtered_button(self):
        self.get_show_filtered_button().click()
        print("Click show all by filter button")

    def click_buy_product(self):
        self.get_buy_product().click()
        print("Click buy product")

    def click_cart(self):
        self.get_cart().click()
        print("Click cart")

    def click_show_all_vendors_smartphones(self):
        self.get_show_all_vendors_smartphones().click()
        print("Click show all vendors smartphones")

    def click_samsung_checkbox(self):
        self.get_samsung_checkbox().click()
        print("Click samsung checkbox")

    def click_smartphones_storage_filter(self):
        self.get_smartphones_storage_filter().click()
        print("Click smartphones storage filter")

    def click_storage_256(self):
        self.get_storage_256().click()
        print("Click storage 256")

    def click_add_to_comparison_1(self):
        self.get_add_to_comparison_1().click()
        print("Click add to comparison 1")

    def click_add_to_comparison_2(self):
        self.get_add_to_comparison_2().click()
        print("Click add to comparison 2")

    def click_comparison(self):
        self.get_comparison().click()
        print("Click comparison")

    def click_add_to_wishlist_1(self):
        self.get_add_to_wishlist_1().click()
        print("Click add to wishlist 1")

    def click_add_to_wishlist_2(self):
        self.get_add_to_wishlist_2().click()
        print("Click add to wishlist 2")

    def click_add_to_wishlist_3(self):
        self.get_add_to_wishlist_3().click()
        print("Click add to wishlist 3")

    def click_wishlist(self):
        self.get_wishlist().click()
        print("Click wishlist")

    # Methods

    def input_price_range(self):
        self.get_current_url()
        self.input_min_price()
        self.input_max_price()

    def set_filters_videocards(self):
        self.click_show_all_vendors_videocards()
        self.click_palit_checkbox()
        self.click_nvidia_checkbox()
        self.click_show_all_series_videocards()
        self.click_series_videocards_1()
        self.click_series_videocards_2()
        self.click_show_all_models_videocards()
        self.click_model_videocard_1()
        self.click_model_videocard_2()
        self.click_model_videocard_3()
        time.sleep(2)  # на случай, чтобы тест не падал, иногда не успевает появиться кнопка
        self.click_show_filtered_button()

    def set_filters_smartphones(self):
        self.click_show_all_vendors_smartphones()
        self.click_samsung_checkbox()
        self.click_smartphones_storage_filter()
        self.click_storage_256()
        time.sleep(2)  # на случай, чтобы тест не падал, иногда не успевает появиться кнопка
        self.click_show_filtered_button()

    # Сохранение названий товаров и их цен в переменные
    def get_product_name_on_page_1(self):
        product_name_on_page = self.get_product_name_1().text
        return product_name_on_page

    def get_product_price_on_page_1(self):
        product_price_on_page = self.get_product_price_1().text
        return product_price_on_page

    def get_product_name_on_page_2(self):
        product_name_on_page = self.get_product_name_2().text
        return product_name_on_page

    def get_product_price_on_page_2(self):
        product_price_on_page = self.get_product_price_2().text
        return product_price_on_page

    def get_product_name_on_page_3(self):
        product_name_on_page = self.get_product_name_3().text
        return product_name_on_page

    def get_product_price_on_page_3(self):
        product_price_on_page = self.get_product_price_3().text
        return product_price_on_page

    def buy_1_product(self):
        self.click_buy_product()
        time.sleep(3)  # без этого товар может не успеть добавиться в корзину
        self.click_cart()

    def buy_several_products(self):
        for i in range(3):
            self.click_buy_product()
            time.sleep(1)
        time.sleep(3)  # без этого товар может не успеть добавиться в корзину
        self.click_cart()

    def add_to_comparison(self):
        self.click_add_to_comparison_1()
        self.click_add_to_comparison_2()
        time.sleep(1)  # без этого товар может не успеть добавиться в сравнение
        self.click_comparison()

    def add_to_wishlist(self):
        self.click_add_to_wishlist_3()  # в обратном порядке, чтобы в вишлисте был такой же порядок, как и на стр товаров
        time.sleep(1)
        self.click_add_to_wishlist_2()
        time.sleep(1)
        self.click_add_to_wishlist_1()
        time.sleep(1)
        self.click_wishlist()
