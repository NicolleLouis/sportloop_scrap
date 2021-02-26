import time

from django.core.management.base import BaseCommand

from campsider.repositories.product_repository import ProductRepository
from campsider.services.scrap_service import ScrapService


class Command(BaseCommand):
    help = 'Test campsider page'

    def handle(self, *args, **options):
        products = ProductRepository.get_unscrapped_product(1)
        driver = ScrapService.create_driver()
        for product in products:
            ScrapService.scrap_individual_product_page(
                product=product,
                driver=driver,
            )
        driver.close()
