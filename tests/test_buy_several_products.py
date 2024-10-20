import time

from pages.cart_page import CartPage
from pages.components_page import ComponentsPage
from pages.main_page import MainPage
from pages.pc_components_page import PcComponentsPage
from pages.products_page import ProductsPage


def test_buy_several_products(set_group):
    driver = set_group

    print("Start TEST BUY SEVERAL PRODUCTS")

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
    # получаем названия и цены товаров на стр товаров из products_page
    product_name_on_page_1 = pp.get_product_name_on_page_1()
    product_price_on_page_1 = pp.get_product_price_on_page_1()
    product_name_on_page_2 = pp.get_product_name_on_page_2()
    product_price_on_page_2 = pp.get_product_price_on_page_2()
    product_name_on_page_3 = pp.get_product_name_on_page_3()
    product_price_on_page_3 = pp.get_product_price_on_page_3()
    pp.buy_several_products()

    # создаем список словарей с полученными названиями и ценами товаров из products_page для сравнения с корзиной
    expected_items = [
        {'name': product_name_on_page_1, 'price': product_price_on_page_1},
        {'name': product_name_on_page_2, 'price': product_price_on_page_2},
        {'name': product_name_on_page_3, 'price': product_price_on_page_3}
    ]

    cp = CartPage(driver)
    cp.cart_check_several_products(expected_items)

    time.sleep(5)
    print("Finish test")
    driver.close()
