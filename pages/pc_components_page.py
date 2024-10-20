from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from base.base_class import Base


class PcComponentsPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    video_cards = "//li[@id='bx_1847241719_13529']"

    # Getters

    def get_video_cards(self): return WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, self.video_cards)))

    # Actions

    def click_video_cards(self):
        self.get_video_cards().click()
        print("Click video cards")

    # Methods

    def choose_video_cards(self):
        self.get_current_url()
        self.assert_url("https://shop.kz/catalog/vse-dlya-sborki-kompyutera/")
        self.click_video_cards()
