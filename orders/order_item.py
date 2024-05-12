from products.hardware import Hardware
from taxes.taxable import Taxable


class OrderItem:
    static_line_num = 1

    def __init__(self, product, quantity):
        self.__product = product
        self.__quantity = quantity
        self.__line_num = OrderItem.static_line_num
        OrderItem.static_line_num += 1

    # Accessors
    def get_product(self):
        return self.__product

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def get_line_num(self):
        return self.__line_num

    # extra functions
    def calc_unit_price(self):
        return self.__product.get_product_retail_price()

    def calc_item_tax(self):
        # check for product type
        if isinstance(self.__product, Taxable):
            return self.__product.get_tax( self.__quantity * self.calc_unit_price() )  # calc
        else:
            return 0

    def calc_item_total(self):
        return self.calc_unit_price() * self.__quantity + self.calc_item_tax()



