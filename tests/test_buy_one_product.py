import time

from pages.cart_page import CartPage
from pages.components_page import ComponentsPage
from pages.main_page import MainPage
from pages.pc_components_page import PcComponentsPage
from pages.products_page import ProductsPage


def test_buy_one_product(set_group):
    driver = set_group

    print("Start TEST BUY ONE PRODUCT")

    mp = MainPage(driver)
    mp.enter_page()
    mp.select_catalog()

    cp = ComponentsPage(driver)
    cp.choose_pc_components()

    pcp = PcComponentsPage(driver)
    pcp.choose_video_cards()

    pp = ProductsPage(driver)
    pp.input_price_range()
    pp.set_filters_videocards()
    product_name_on_page = pp.get_product_name_on_page_1()  # получаем название товара на странице товаров из products_page
    product_price_on_page = pp.get_product_price_on_page_1()  # получаем цену товара на странице товаров из products_page
    pp.buy_1_product()

    cp = CartPage(driver)
    cp.cart_check_one_product(product_name_on_page, product_price_on_page)

    time.sleep(5)
    print("Finish test")
    driver.close()
