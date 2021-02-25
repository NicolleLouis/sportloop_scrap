import time

from django.core.management.base import BaseCommand
from selenium import webdriver

from campsider.services.scrap_service import ScrapService


class Command(BaseCommand):
    help = 'Test campsider page'

    def handle(self, *args, **options):
        urls = [
            "https://www.campsider.com/genre/homme",
            "https://www.campsider.com/genre/femme",
            "https://www.campsider.com/genre/enfant",
            "https://www.campsider.com/sport/ski-snow",
            "https://www.campsider.com/sport/randonnee-trekking",
            "https://www.campsider.com/sport/vtt",
        ]
        for url in urls:
            ScrapService.scrap_product_from_all_page(url)
