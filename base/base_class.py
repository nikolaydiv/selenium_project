import datetime


class Base():

    def __init__(self, driver):
        self.driver = driver

    # Method GET CURRENT URL
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Current url: {get_url}')

    # Method ASSERT WORD
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")

    # Method ASSERT URL
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")

    # Method GET SCREENSHOT
    def get_screenshot_buy_one_product(self):
        now_date = datetime.datetime.now().strftime("%d.%m.%Y.%H.%M.%S")
        name_screenshot = f"screenshot_{now_date}.png"
        self.driver.save_screenshot('C:\\Users\\dvd10\\PycharmProjects\\final_project_selenium_automation\\screen\\buy_one_product\\' + name_screenshot)

    def get_screenshot_buy_several_products(self):
        now_date = datetime.datetime.now().strftime("%d.%m.%Y.%H.%M.%S")
        name_screenshot = f"screenshot_{now_date}.png"
        self.driver.save_screenshot('C:\\Users\\dvd10\\PycharmProjects\\final_project_selenium_automation\\screen\\buy_several_products\\' + name_screenshot)

    def get_screenshot_compare_products(self):
        now_date = datetime.datetime.now().strftime("%d.%m.%Y.%H.%M.%S")
        name_screenshot = f"screenshot_{now_date}.png"
        self.driver.save_screenshot('C:\\Users\\dvd10\\PycharmProjects\\final_project_selenium_automation\\screen\\compare_products\\' + name_screenshot)

    def get_screenshot_wishlist(self):
        now_date = datetime.datetime.now().strftime("%d.%m.%Y.%H.%M.%S")
        name_screenshot = f"screenshot_{now_date}.png"
        self.driver.save_screenshot('C:\\Users\\dvd10\\PycharmProjects\\final_project_selenium_automation\\screen\\wishlist\\' + name_screenshot)
