class Item:
    def __init__(self, code, title, description, category, picture, quantity_in_stock, price):
        self.code = code
        self.title = title
        self.description = description
        self.category = category
        self.picture = picture
        self.quantity_in_stock = quantity_in_stock
        self.price = price
        
    def view_full_description(self):
        # logic for displaying full item description
        pass
    
    def add_to_cart(self):
        # logic for adding item to cart
        pass
    
    def update_stock_level(self):
        # logic for updating stock level
        pass