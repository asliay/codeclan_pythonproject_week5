class Album:

    def __init__(self, title, artist, genre, price, cost_price, release_year, stock, label, id=None):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.price = price
        self.cost_price = cost_price
        self.release_year = release_year
        # self.cover_art = cover_art
        self.label = label
        self.stock = stock
        self.id = id
         


    # increase stock 
    # def order_stock(self, amount):
    #     self.stock += amount

    # # decrease stock
    # def sell_stock(self, amount):
    #     self.stock -= amount
