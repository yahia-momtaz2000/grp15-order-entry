from abc import ABC


class Customer(ABC):
    def __init__(self, customer_id, customer_name, customer_phone, customer_address):
        self.__customer_id = customer_id
        self.__customer_name = customer_name
        self.__customer_phone = customer_phone
        self.__customer_address = customer_address

    # Accessors

    def get_customer_id(self):
        return self.__customer_id

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def get_customer_name(self):
        return self.__customer_name

    def set_customer_name(self, customer_name):
        self.__customer_name = customer_name

    def get_customer_phone(self):
        return self.__customer_phone

    def set_customer_phone(self, customer_phone):
        self.__customer_phone = customer_phone

    def get_customer_address(self):
        return self.__customer_address

    def set_customer_address(self, customer_address):
        self.__customer_address = customer_address


