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

    @staticmethod
    def get_unscrapped_product(limit_number=None):
        product_list = Product.objects.filter(is_scrapped=False)
        if limit_number is not None:
            product_list = product_list[:limit_number]
        return list(product_list)
