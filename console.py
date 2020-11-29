import pdb
from models.album import Album
from models.artist import Artist
# from models.label import Label

import repositories.artist_repository as artist_repository
# import repositories.label_repository as label_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
# label_repository.delete_all()
artist_repository.delete_all()

# ARTISTS

biffy = Artist("Biffy Clyro")
artist_repository.save(biffy)
dire_straits = Artist("Dire Straits")
artist_repository.save(dire_straits)
fleetwood_mac = Artist("Fleetwood Mac")
artist_repository.save(fleetwood_mac)
frightened_rabbit = Artist("Frightened Rabbit")
artist_repository.save(frightened_rabbit)
hozier = Artist("Hozier")
artist_repository.save(hozier)
leonard_cohen = Artist("Leonard Cohen")
artist_repository.save(leonard_cohen)
maggie_rogers = Artist("Maggie Rogers")
artist_repository.save(maggie_rogers)
paramore = Artist("Paramore")
artist_repository.save(paramore)
phoebe_bridgers = Artist("Phoebe Bridgers")
artist_repository.save(phoebe_bridgers)
sara = Artist("Sara Bareilles")
artist_repository.save(sara)
tallest_man = Artist("The Tallest Man on Earth")
artist_repository.save(tallest_man)





# # LABELS
# fourteenth = Label("14th Floor (Warner)")
# label_repository.save(fourteenth)
# atlantic = Label("Atlantic Records")
# label_repository.save(atlantic)
# capitol = Label("Capitol Records")
# label_repository.save(capitol)
# columbia = Label("Columbia Records")
# label_repository.save(columbia)
# dead_oceans = Label("Dead Oceans")
# label_repository.save(dead_oceans)
# epic = Label("Epic Records (Sony)")
# label_repository.save(epic)
# fat_cat = Label("Fat Cat Records")
# label_repository.save(fat_cat)
# fueled_by_ramen = Label("Fueled By Ramen")
# label_repository.save(fueled_by_ramen)
# island = Label("Island Records")
# label_repository.save(island)
# sony = Label("Sony Music")
# label_repository.save(sony)
# universal = Label("Universal Music")
# label_repository.save(universal)
# vertigo = Label("Vertigo")
# label_repository.save(vertigo)
# virgin = Label("Virgin Records")
# label_repository.save(virgin)
# warner = Label("Warner Records")
# label_repository.save(warner)




# ALBUMS

# Biffy Clyro Albums

endings = Album("A Celebration of Endings", biffy, "Alternative Rock", 24.99, 14.99, "2020", 7, "14th Floor")
album_repository.save(endings)
ellipsis = Album("Ellipsis", biffy, "Alternative Rock", 19.99, 11.99, "2016", 8, "14th Floor")
album_repository.save(ellipsis)
opposites = Album("Opposites", biffy, "Alternative Rock", 22.99, 13.79, "2013", 9, "14th Floor")
album_repository.save(opposites)
revolutions = Album("Only Revolutions", biffy, "Alternative Rock", 19.99, 11.99, "2009", 5, "14th Floor")
album_repository.save(revolutions)
puzzle = Album("Puzzle", biffy, "Alternative Rock", 27.99, 16.79, "2007", 3, "14th Floor")
album_repository.save(puzzle)

# Dire Straits Albums
brothers = Album("Brothers in Arms", dire_straits, "Rock", 25.99, 15.59, "1985", 6, "Vertigo")
album_repository.save(brothers)
making_movies = Album("Making Movies", dire_straits, "Rock", 24.99, 14.99, "1980", 2, "Vertigo")
album_repository.save(making_movies)

# Fleetwood Mac Albums 
tango = Album("Tango in the Night", fleetwood_mac, "Pop Rock", 20.00, 12.00, "1987", 8, "Warner Records")
album_repository.save(tango)
mirage = Album("Mirage", fleetwood_mac, "Soft Rock", 20.00, 12.00, "1982", 7, "Warner Records")
album_repository.save(mirage)
tusk = Album("Tusk", fleetwood_mac, "Rock", 20.00, 12.00, "1979", 2, "Warner Records")
album_repository.save(tusk)
rumours = Album("Rumours", fleetwood_mac, "Folk Rock", 20.00, 12.00, "1977", 15, "Warner Records")
album_repository.save(rumours)
fleetwood_self_titled = Album("Fleetwood Mac", fleetwood_mac, "Soft Rock", 20.00, 12.00, "1975", 8, "Warner Records")
album_repository.save(fleetwood_self_titled)

# Frightened Rabbit Albums
panic_attack = Album("Painting of a Panic Attack", frightened_rabbit, "Indie Rock", 21.99, 13.19, "2016", 15, "Atlantic Records")
album_repository.save(panic_attack)
pedestrian = Album("Pedestrian Verse", frightened_rabbit, "Indie Rock", 19.99, 11.99, "2013", 1, "Atlantic Records")
album_repository.save(pedestrian)
midnight = Album("Midnight Organ Fight", frightened_rabbit, "Indie Rock", 22.99, 13.79, "2008", 0, "Fat Cat Records")
album_repository.save(midnight)

# Hozier Albums
wasteland = Album("Wasteland, Baby!", hozier, "Soul", 24.99, 14.99, "2019", 3, "Island Records")
album_repository.save(wasteland)
hozier_self_titled = Album("Hozier", hozier, "Folk Rock", 24.99, 14.99, "2014", 2, "Island Records")
album_repository.save(hozier_self_titled)


# Leonard Cohen Albums
thanks_for_the_dance = Album("Thanks for the Dance", leonard_cohen, "Folk Rock", 20.00, 12.00, "2019", 11, "Columbia Records")
album_repository.save(thanks_for_the_dance)
darker = Album("You Want it Darker", leonard_cohen, "Folk Rock", 20.00, 12.00, "2016", 10, "Columbia Records")
album_repository.save(darker)
future = Album("The Future", leonard_cohen, "Soft Rock", 20.00, 12.00, "1992", 12, "Columbia Records")
album_repository.save(future)
your_man = Album("I'm Your Man", leonard_cohen, "Soft Rock", 20.00, 12.00, "1988", 0, "Columbia Records")
album_repository.save(your_man)
various_positions = Album("Various Positions", leonard_cohen, "Folk", 20.00, 12.00, "1985", 12, "Columbia Records")
album_repository.save(various_positions)
love_and_hate = Album("Songs of Love and Hate", leonard_cohen, "Folk", 20.00, 12.00, "1971", 9, "Columbia Records")
album_repository.save(love_and_hate)
from_a_room = Album("Songs from a Room", leonard_cohen, "Folk", 20.00, 12.00, "1969", 2,"Columbia Records")
album_repository.save(from_a_room)
songs_of = Album("Songs of Leonard Cohen", leonard_cohen, "Folk", 20.00, 12.00, "1967", 7, "Columbia Records")
album_repository.save(songs_of)

# Maggie Rogers Album
past_life = Album("Heard it in a Past Life", maggie_rogers, "Folk Pop", 19.99, 11.99, "2019", 3, "Capitol Records")
album_repository.save(past_life)


# Paramore Albums
after_laughter = Album("After Laughter", paramore, "Pop Rock", 17.99, 10.79, "2017", 15, "Fueled By Ramen")
album_repository.save(after_laughter)
paramore_self_titled = Album("Paramore", paramore, "Pop Rock", 17.99, 10.79, "2013", 4, "Fueled By Ramen")
album_repository.save(paramore_self_titled)
brand_new_eyes = Album("Brand New Eyes", paramore, "Pop Rock", 17.99, 10.79, "2009", 2, "Fueled By Ramen")
album_repository.save(brand_new_eyes)
riot = Album("Riot!", paramore, "Alt-Rock", 17.99, 10.79, "2007", 1, "Fueled By Ramen")
album_repository.save(riot)
falling = Album("All We Know is Falling", paramore, "Alt-Rock", 17.99, 10.79, "2005", 8, "Fueled By Ramen")
album_repository.save(falling)

# Phoebe Bridgers Albums
punisher = Album("Punisher", phoebe_bridgers, "Indie Rock", 21.99, 13.19, "2020", 6, "Dead Oceans")
album_repository.save(punisher)
stranger = Album("Stranger in the Alps", phoebe_bridgers, "Indie Rock", 21.99, 13.19, "2017", 5, "Dead Oceans")
album_repository.save(stranger)

# Tallest Man on Earth Album

fever_dream = Album("I Love You. It's a Fever Dream.", tallest_man, "Folk", 17.99, 10.79, "2019", 2, "Dead Oceans")
album_repository.save(fever_dream)



pdb.set_trace()



