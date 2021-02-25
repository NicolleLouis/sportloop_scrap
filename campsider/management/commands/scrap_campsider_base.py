import time

from django.core.management.base import BaseCommand
from selenium import webdriver
from bs4 import BeautifulSoup


class Command(BaseCommand):
    help = 'Test campsider page'

    def handle(self, *args, **options):
        base_url = "https://www.campsider.com/genre/homme"

        driver = webdriver.Chrome(executable_path="/home/louis/App/chromedriver")
        driver.get(base_url)
        time.sleep(10)

        list_product = driver.find_elements_by_class_name("RepeatingGroup")
        list_product = list(
            map(
                lambda element: element.get_attribute('innerHTML'),
                list_product
            )
        )
        soup = BeautifulSoup(list_product[0], 'html.parser')
        items = soup.find_all("a")
        print(len(items))
        driver.close()
