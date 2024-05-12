from datetime import datetime

from orders.order_item import OrderItem


class Order:
    def __init__(self, order_id, customer):
        self.__order_id = order_id
        self.__customer = customer
        self.__items_list = []
        self.__order_date = datetime.now()
        self.__order_total = 0.0

    # Accessors
    def get_order_id(self):
        return self.__order_id

    def get_order_date(self):
        return self.__order_date

    def get_customer(self):
        return self.__customer

    def get_order_total(self):
        total = 0
        for item in self.__items_list:
            total = total + item.calc_item_total()

        self.__order_total = total
        return self.__order_total

    # Extra functions
    def add_product_to_cart(self, new_product):  # append new product to items_list
        # Check for this product if already found in the list or not
        is_found = False
        for item in self.__items_list:
            if new_product.get_product_name() == item.get_product().get_product_name(): # already found
                is_found = True
                current_quantity = item.get_quantity()
                item.set_quantity(current_quantity + 1)

        if is_found == False:
            item = OrderItem(new_product, 1)        # create new object [ new line ]
            self.__items_list.append(item)

    def preview_order(self):
        print('---------- Order data ---------')
        print('Order id = ', self.__order_id)
        print('Order date = ', self.__order_date.date())
        print('Customer name = ', self.__customer.get_customer_name())
        print('Order Total = ', self.get_order_total())
        print('----- Order items Lines ----')
        for item in self.__items_list:
            print('line num = ', item.get_line_num())
            print('product name = ', item.get_product().get_product_name())
            print('quantity = ', item.get_quantity())
            print('Unit price = ', item.calc_unit_price())
            print('Item Tax = ', item.calc_item_tax())
            print('Item total = ', item.calc_item_total())
            print('------------')




