class Order:
    def __init__(self, date, status, shopping_cart, delivery_address, payment_method):
        self.date = date
        self.status = status
        self.shopping_cart = shopping_cart
        self.delivery_address = delivery_address
        self.payment_method = payment_method

    def validatePayment(self):
        # TODO: Implement payment validation logic
        pass

    def cancel(self):
        self.status = "Cancelled"

    def dispatch(self):
        self.status = "Dispatched"

    def confirmDelivery(self):
        self.status = "Delivered"

    def refund(self):
        # TODO: Implement refund logic
        pass

    def archive(self):
        # TODO: Implement archive logic
        pass
