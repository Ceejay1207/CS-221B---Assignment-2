from Item import Item

class MP3(Item):
    def __init__(self, code, title, description, category, picture, quantity_in_stock, price, duration, artist):
        super().__init__(code, title, description, category, picture, quantity_in_stock, price)
        self.duration = duration
        self.artist = artist
        
    def play_extract(self):
        # logic for playing MP3 extract
        pass
    
    def download(self):
        # logic for downloading MP3 file
        pass

mp3_item = MP3(code="MP3-001", 
               title="Perfect", 
               description="The song is a romantic ballad focusing on traditional marriage.", 
               category="Pop", 
               picture="https://example.com/image.jpg", 
               quantity_in_stock=100, 
               price=9.99, 
               duration="4:23", 
               artist="Ed Sheeran")

# Access the attribute values
print(mp3_item.code)
print(mp3_item.title)
print(mp3_item.description)
print(mp3_item.category)
print(mp3_item.picture)
print(mp3_item.quantity_in_stock)
print(mp3_item.price)
print(mp3_item.duration)
print(mp3_item.artist)

