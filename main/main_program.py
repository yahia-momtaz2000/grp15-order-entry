from customers.customer import Customer
from orders.order import Order
from products.hardware import Hardware
from products.software import Software

# main program
# create stock items
keyboard = Hardware(1, "keyboard", 100, "accessories", 3)
office2022 = Software(2, "office 2022", 200, "Ms Office", "554-65-211")
printer_canon = Hardware(3, "Canon printer", 500, "printers", 10)

# create a customer
raya = Customer(100, "Raya", "01012312312", "Cairo")

# create new order
order1001 = Order(1001, raya)
order1001.add_product_to_cart(keyboard)
order1001.add_product_to_cart(keyboard)

order1001.add_product_to_cart(keyboard)
order1001.add_product_to_cart(office2022)

# preview Order
order1001.preview_order()
