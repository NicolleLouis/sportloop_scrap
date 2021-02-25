from bs4 import BeautifulSoup

from campsider.repositories.product_repository import ProductRepository


class ScrapService:
    @staticmethod
    def get_or_create_product_from_page(driver):
        product_list = driver.find_elements_by_class_name("RepeatingGroup")
        product_list = list(
            map(
                lambda element: element.get_attribute('innerHTML'),
                product_list
            )
        )[0]

        soup = BeautifulSoup(product_list, 'html.parser')
        items = soup.find_all("a")
        for item in items:
            url = item["href"]
            ProductRepository.get_or_create_by_url(url)
