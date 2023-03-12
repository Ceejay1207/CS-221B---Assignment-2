from Item import Item


class DVD(Item):
    def __init__(self, code, title, description, category, picture, quantity_in_stock, price, director, certificate, list_of_actors):
        super().__init__(code, title, description, category, picture, quantity_in_stock, price)
        self.director = director
        self.certificate = certificate
        self.list_of_actors = list_of_actors

# Create an instance of the DVD class
dvd = DVD(
    code="DVD001",
    title="The Matrix",
    description="A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
    category="Action",
    picture="https://www.example.com/images/the-matrix.jpg",
    quantity_in_stock=10,
    price=12.99,
    director="The Wachowskis",
    certificate="R",
    list_of_actors=["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"]
)

# Access the attribute values
print(dvd.code)
print(dvd.title)
print(dvd.description)
print(dvd.category)
print(dvd.picture)
print(dvd.quantity_in_stock)
print(dvd.price)
print(dvd.director)
print(dvd.certificate)
print(dvd.list_of_actors)
