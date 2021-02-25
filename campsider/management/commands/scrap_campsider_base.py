import time

from django.core.management.base import BaseCommand
from selenium import webdriver

from campsider.services.scrap_service import ScrapService


class Command(BaseCommand):
    help = 'Test campsider page'

    def handle(self, *args, **options):
        base_url = "https://www.campsider.com/genre/homme"

        driver = webdriver.Chrome(executable_path="/home/louis/App/chromedriver")
        driver.get(base_url)
        time.sleep(10)

        ScrapService.get_or_create_product_from_page(driver=driver)
        next = driver.find_elements_by_class_name("fa-angle-right")[0]
        print(next)
        next.click()
        time.sleep(10)

        driver.close()
