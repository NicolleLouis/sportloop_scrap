from django.core.management.base import BaseCommand
from selenium import webdriver


class Command(BaseCommand):
    help = 'Test campsider page'

    def handle(self, *args, **options):
        base_url = "https://www.campsider.com/genre/homme"

        driver = webdriver.Chrome(executable_path="/home/louis/App/chromedriver")
        driver.get(base_url)
        list_product = driver.find_elements_by_class_name("RepeatingGroup")
        list_product = list(
            map(
                lambda element: element.get_attribute('innerHTML'),
                list_product
            )
        )
        print(list_product)
