from campsider.models.product import Product


class ProductRepository:
    @staticmethod
    def get_or_create_by_url(
            url
    ):
        product, _created = Product.objects.get_or_create(
            url=url
        )
        return url, _created

    @staticmethod
    def get_product():
        return list(Product.objects.all())
