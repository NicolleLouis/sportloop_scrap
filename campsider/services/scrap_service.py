import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

from campsider.repositories.product_repository import ProductRepository


class ScrapService:
    @staticmethod
    def create_driver():
        driver = webdriver.Chrome(executable_path="/home/louis/App/chromedriver")
        return driver

    @staticmethod
    def scrap_product_from_all_page(base_url):
        driver = ScrapService.create_driver()
        driver.get(base_url)
        time.sleep(5)

        while True:
            try:
                ScrapService.scrap_product_from_page(driver=driver)
                next_button = driver.find_elements_by_class_name("fa-angle-right")[0]
                if not ScrapService.is_next_button_is_clickable(next_button):
                    break
                next_button.click()
                time.sleep(2)
            except:
                break

        driver.close()

    @staticmethod
    def scrap_product_from_page(driver):
        product_list = driver.find_elements_by_class_name("RepeatingGroup")[0]
        product_list = product_list.get_attribute('innerHTML')

        soup = BeautifulSoup(product_list, 'html.parser')
        items = soup.find_all("a")
        for item in items:
            url = item["href"]
            ProductRepository.get_or_create_by_url(url)

    @staticmethod
    def is_next_button_is_clickable(next_button):
        return next_button.value_of_css_property("cursor") == "pointer"

    @staticmethod
    def scrap_individual_product_page(
            product,
            driver
    ):
        driver.get(product.url)
        time.sleep(2)
        data = driver.find_element_by_xpath(
            "//div[@class='main-page bubble-element Page']/div[2]"
        )
        data = data.find_element(By.CLASS_NAME, "Group")
        print(data.get_attribute('innerHTML'))
