from pages.comparison_page import ComparisonPage
from pages.main_page import MainPage
from pages.products_page import ProductsPage


def test_compare_products(set_group):
    driver = set_group

    print("Start TEST COMPARE PRODUCTS")

    mp = MainPage(driver)
    mp.enter_page()
    mp.select_smartphones()

    pp = ProductsPage(driver)
    pp.input_price_range()
    pp.set_filters_smartphones()
    product_name_on_page_1 = pp.get_product_name_on_page_1()
    product_price_on_page_1 = pp.get_product_price_on_page_1().replace(" ₸", "")  # убираем знак валюты для assert (знак валюты отличается от сравнения)
    product_name_on_page_2 = pp.get_product_name_on_page_2()
    product_price_on_page_2 = pp.get_product_price_on_page_2().replace(" ₸", "")
    pp.add_to_comparison()

    cp = ComparisonPage(driver)
    cp.check_comparison()
    assert product_name_on_page_1 == cp.get_compare_product_name_1().text
    print(f"Название товара 1 {product_name_on_page_1} совпадает")
    assert product_price_on_page_1 == cp.get_compare_product_price_1().text.replace(" т", "")  # убираем знак валюты для assert (знак валюты отличается от страницы)
    print(f"Цена товара 1 {product_price_on_page_1} совпадает")
    assert product_name_on_page_2 == cp.get_compare_product_name_2().text
    print(f"Название товара 2 {product_name_on_page_2} совпадает")
    assert product_price_on_page_2 == cp.get_compare_product_price_2().text.replace(" т", "")
    print(f"Цена товара 2 {product_price_on_page_2} совпадает")
    cp.delete_comparing_products()

    print("Finish test")
    driver.close()
