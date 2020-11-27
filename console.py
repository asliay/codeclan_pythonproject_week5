import pdb
from models.album import Album
from models.artist import Artist
from models.label import Label

import repositories.artist_repository as artist_repository
import repositories.label_repository as label_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
label_repository.delete_all()
artist_repository.delete_all()

# ARTISTS
paramore = Artist("Paramore")
artist_repository.save(paramore)
leonard_cohen = Artist("Leonard Cohen")
artist_repository.save(leonard_cohen)
fleetwood_mac = Artist("Fleetwood Mac")
artist_repository.save(fleetwood_mac)

# LABELS
fueled_by_ramen = Label("Fueled By Ramen")
label_repository.save(fueled_by_ramen)
columbia = Label("Columbia Records")
label_repository.save(columbia)
warner = Label("Warner Records")
label_repository.save(warner)

# ALBUMS

#Paramore Albums
after_laughter = Album("After Laughter", paramore, "Pop Rock", 17.99, 10.79, "2017", fueled_by_ramen)
album_repository.save(after_laughter)
paramore_self_titled = Album("Paramore", paramore, "Pop Rock", 17.99, 10.79, "2013", fueled_by_ramen)
album_repository.save(paramore_self_titled)
brand_new_eyes = Album("Brand New Eyes", paramore, "Pop Rock", 17.99, 10.79, "2009", fueled_by_ramen)
album_repository.save(brand_new_eyes)
riot = Album("Riot!", paramore, "Alt-Rock", 17.99, 10.79, "2007", fueled_by_ramen)
album_repository.save(riot)
falling = Album("All We Know is Falling", paramore, "Alt-Rock", 17.99, 10.79, "2005", fueled_by_ramen)
album_repository.save(falling)

#Leonard Cohen Albums
thanks_for_the_dance = Album("Thanks for the Dance", leonard_cohen, "Folk Rock", 20.00, 12.00, "2019", columbia)
album_repository.save(thanks_for_the_dance)
darker = Album("You Want it Darker", leonard_cohen, "Folk Rock", 20.00, 12.00, "2016", columbia)
album_repository.save(darker)
future = Album("The Future", leonard_cohen, "Soft Rock", 20.00, 12.00, "1992", columbia)
album_repository.save(future)
your_man = Album("I'm Your Man", leonard_cohen, "Soft Rock", 20.00, 12.00, "1988", columbia)
album_repository.save(your_man)
various_positions = Album("Various Positions", leonard_cohen, "Folk", 20.00, 12.00, "1985", columbia)
album_repository.save(various_positions)
love_and_hate = Album("Songs of Love and Hate", leonard_cohen, "Folk", 20.00, 12.00, "1971", columbia)
album_repository.save(love_and_hate)
from_a_room = Album("Songs from a Room", leonard_cohen, "Folk", 20.00, 12.00, "1969", columbia)
album_repository.save(from_a_room)
songs_of = Album("Songs of Leonard Cohen", leonard_cohen, "Folk", 20.00, 12.00, "1967", columbia)
album_repository.save(songs_of)

# Fleetwood Mac Albums 
tango = Album("Tango in the Night", fleetwood_mac, "Pop Rock", 20.00, 12.00, "1987", warner)
album_repository.save(tango)
mirage = Album("Mirage", fleetwood_mac, "Soft Rock", 20.00, 12.00, "1982", warner)
album_repository.save(mirage)
tusk = Album("Tusk", fleetwood_mac, "Rock", 20.00, 12.00, "1979", warner)
album_repository.save(tusk)
rumours = Album("Rumours", fleetwood_mac, "Folk Rock", 20.00, 12.00, "1977", warner)
album_repository.save(rumours)
fleetwood_self_titled = Album("Fleetwood Mac", fleetwood_mac, "Soft Rock", 20.00, 12.00, "1975", warner)
album_repository.save(fleetwood_self_titled)






pdb.set_trace()



