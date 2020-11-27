class Album:

    def __init__(self, title, artist, genre, price, cost_price, release_year, label, id=None):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.price = price
        self.cost_price = cost_price
        self.release_year = release_year
        self.label = label
        self.id = id
        self.stock = 0


    # increase stock 
    # def order_stock(self, amount):
    #     self.stock += amount

    # # decrease stock
    # def sell_stock(self, amount):
    #     self.stock -= amount
