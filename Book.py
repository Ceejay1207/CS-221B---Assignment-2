from Item import Item

class Book(Item):
    def __init__(self, code, title, description, category, picture, quantity_in_stock, price, isbn, author, synopsis):
        super().__init__(code, title, description, category, picture, quantity_in_stock, price)
        self.isbn = isbn
        self.author = author
        self.synopsis = synopsis
        
    def preview(self):
        # logic for showing book preview
        pass
    
    # Creating an instance of Book class
my_book = Book(code="B001", 
    title="The Hitchhiker's Guide to the Galaxy", 
    description="A science fiction comedy series", 
    category="Science Fiction", 
    picture="https://example.com/hitchhiker.jpg", 
    quantity_in_stock=10, 
    price=9.99, 
    isbn="978-0345391803", 
    author="Douglas Adams", 
    synopsis="The story follows the misadventures of the last surviving man, Arthur Dent, and his alien friend, Ford Prefect, as they travel through space after Earth is destroyed to make way for a hyperspace bypass.")

# Accessing the attributes of my_book instance
print(my_book.code)              # Output: B001
print(my_book.title)             # Output: The Hitchhiker's Guide to the Galaxy
print(my_book.category)          # Output: Science Fiction
print(my_book.price)             # Output: 9.99
print(my_book.author)            # Output: Douglas Adams
print(my_book.synopsis)          # Output: The story follows the misadventures of the last surviving man, Arthur Dent, and his alien friend, Ford Prefect, as they travel through space after Earth is destroyed to make way for a hyperspace bypass.
