from products.product import Product


class Manual(Product):
    def __init__(self, product_id, product_name, product_retail_price, product_description, publisher):
        super().__init__(product_id, product_name, product_retail_price, product_description)
        self.__publisher = publisher

    # Accessors
    def get_publisher(self):
        return self.__publisher

    def set_publisher(self, publisher):
        self.__publisher = publisher

