import pdb
from models.album import Album
from models.artist import Artist
from models.label import Label


import repositories.artist_repository as artist_repository
import repositories.label_repository as label_repository
import repositories.album_repository as album_repository

# Clears data from tables
album_repository.delete_all()
label_repository.delete_all()
artist_repository.delete_all()


# ARTISTS - Populates Artists table
biffy = Artist("Biffy Clyro")
artist_repository.save(biffy)
# dire_straits = Artist("Dire Straits")
# artist_repository.save(dire_straits)
# fleetwood_mac = Artist("Fleetwood Mac")
# artist_repository.save(fleetwood_mac)
# frightened_rabbit = Artist("Frightened Rabbit")
# artist_repository.save(frightened_rabbit)
# hozier = Artist("Hozier")
# artist_repository.save(hozier)
# janelle = Artist("Janelle Monáe")
# artist_repository.save(janelle)
# leonard_cohen = Artist("Leonard Cohen")
# artist_repository.save(leonard_cohen)
# lizzo = Artist("Lizzo")
# artist_repository.save(lizzo)
# maggie_rogers = Artist("Maggie Rogers")
# artist_repository.save(maggie_rogers)
# paramore = Artist("Paramore")
# artist_repository.save(paramore)
# phoebe_bridgers = Artist("Phoebe Bridgers")
# artist_repository.save(phoebe_bridgers)
# sara = Artist("Sara Bareilles")
# artist_repository.save(sara)
# tallest_man = Artist("The Tallest Man on Earth")
# artist_repository.save(tallest_man)

# LABELS - class and table removed for now?
fourteenth = Label("14th Floor (Warner)")
label_repository.save(fourteenth)
atlantic = Label("Atlantic Records")
label_repository.save(atlantic)
capitol = Label("Capitol Records")
label_repository.save(capitol)
columbia = Label("Columbia Records")
label_repository.save(columbia)
dead_oceans = Label("Dead Oceans")
label_repository.save(dead_oceans)
epic = Label("Epic Records (Sony)")
label_repository.save(epic)
fat_cat = Label("Fat Cat Records")
label_repository.save(fat_cat)
fueled_by_ramen = Label("Fueled By Ramen")
label_repository.save(fueled_by_ramen)
island = Label("Island Records")
label_repository.save(island)
sony = Label("Sony Music")
label_repository.save(sony)
universal = Label("Universal Music")
label_repository.save(universal)
vertigo = Label("Vertigo")
label_repository.save(vertigo)
virgin = Label("Virgin Records")
label_repository.save(virgin)
warner = Label("Warner Records")
label_repository.save(warner)


# ALBUMS - Populates Albums table

# Biffy Clyro Albums

endings = Album("A Celebration of Endings", biffy, "Alternative Rock", 24.99, 14.99, "2020", "https://is5-ssl.mzstatic.com/image/thumb/Music114/v4/3a/e3/77/3ae37790-7982-c517-02b4-b4ea4b55a7b5/source/600x600bb.jpg", 4, fourteenth)
album_repository.save(endings)
ellipsis = Album("Ellipsis", biffy, "Alternative Rock", 19.99, 11.99, "2016", "https://is2-ssl.mzstatic.com/image/thumb/Music49/v4/7b/29/cd/7b29cd44-0d47-963e-5ffe-89d67c6e7dc4/source/600x600bb.jpg", 5, fourteenth)
album_repository.save(ellipsis)
opposites = Album("Opposites", biffy, "Alternative Rock", 22.99, 13.79, "2013", "https://is3-ssl.mzstatic.com/image/thumb/Music/v4/bc/b0/d7/bcb0d7a1-48f0-63d0-ea4b-a780e8f43dd6/source/600x600bb.jpg", 3, fourteenth)
album_repository.save(opposites)
revolutions = Album("Only Revolutions", biffy, "Alternative Rock", 19.99, 11.99, "2009", "https://is2-ssl.mzstatic.com/image/thumb/Music/v4/d4/ba/68/d4ba6840-7a23-3e3e-eda4-ab39a00fbf30/source/600x600bb.jpg", 2, fourteenth)
album_repository.save(revolutions)
puzzle = Album("Puzzle", biffy, "Alternative Rock", 27.99, 16.79, "2007", "https://is5-ssl.mzstatic.com/image/thumb/Music/v4/fb/27/17/fb2717b4-403d-9aa2-72ca-757849357e5a/source/600x600bb.jpg", 3, fourteenth)
album_repository.save(puzzle)

# # Dire Straits Albums
# brothers = Album("Brothers in Arms", dire_straits, "Rock", 25.99, 15.59, "1985", 1, vertigo)
# album_repository.save(brothers)
# making_movies = Album("Making Movies", dire_straits, "Rock", 24.99, 14.99, "1980", 2, vertigo)
# album_repository.save(making_movies)

# # Fleetwood Mac Albums 
# tango = Album("Tango in the Night", fleetwood_mac, "Pop Rock", 20.00, 12.00, "1987", 4, warner)
# album_repository.save(tango)
# mirage = Album("Mirage", fleetwood_mac, "Soft Rock", 20.00, 12.00, "1982", 0, warner)
# album_repository.save(mirage)
# tusk = Album("Tusk", fleetwood_mac, "Rock", 20.00, 12.00, "1979", 2, warner)
# album_repository.save(tusk)
# rumours = Album("Rumours", fleetwood_mac, "Folk Rock", 20.00, 12.00, "1977", 5, warner)
# album_repository.save(rumours)
# fleetwood_self_titled = Album("Fleetwood Mac", fleetwood_mac, "Soft Rock", 20.00, 12.00, "1975", 3, warner)
# album_repository.save(fleetwood_self_titled)

# # Frightened Rabbit Albums
# panic_attack = Album("Painting of a Panic Attack", frightened_rabbit, "Indie Rock", 21.99, 13.19, "2016", 6, atlantic)
# album_repository.save(panic_attack)
# pedestrian = Album("Pedestrian Verse", frightened_rabbit, "Indie Rock", 19.99, 11.99, "2013", 1, atlantic)
# album_repository.save(pedestrian)
# midnight = Album("Midnight Organ Fight", frightened_rabbit, "Indie Rock", 22.99, 13.79, "2008", 0, fat_cat)
# album_repository.save(midnight)

# # Hozier Albums
# wasteland = Album("Wasteland, Baby!", hozier, "Soul", 24.99, 14.99, "2019", 3, island)
# album_repository.save(wasteland)
# hozier_self_titled = Album("Hozier", hozier, "Folk Rock", 24.99, 14.99, "2014", 2, island)
# album_repository.save(hozier_self_titled)


# # Janelle Monáe Album
# dirty_computer = Album("Dirty Computer", janelle, "Funk/ R&B", 21.99, 13.19, "2018", 1, atlantic)
# album_repository.save(dirty_computer)

# # Leonard Cohen Albums
# thanks_for_the_dance = Album("Thanks for the Dance", leonard_cohen, "Folk Rock", 20.00, 12.00, "2019", 5, columbia)
# album_repository.save(thanks_for_the_dance)
# darker = Album("You Want it Darker", leonard_cohen, "Folk Rock", 20.00, 12.00, "2016", 9, columbia)
# album_repository.save(darker)
# future = Album("The Future", leonard_cohen, "Soft Rock", 20.00, 12.00, "1992", 3, columbia)
# album_repository.save(future)
# your_man = Album("I'm Your Man", leonard_cohen, "Soft Rock", 20.00, 12.00, "1988", 0, columbia)
# album_repository.save(your_man)
# various_positions = Album("Various Positions", leonard_cohen, "Folk", 20.00, 12.00, "1985", 2, columbia)
# album_repository.save(various_positions)
# love_and_hate = Album("Songs of Love and Hate", leonard_cohen, "Folk", 20.00, 12.00, "1971", 8, columbia)
# album_repository.save(love_and_hate)
# from_a_room = Album("Songs from a Room", leonard_cohen, "Folk", 20.00, 12.00, "1969", 2,columbia)
# album_repository.save(from_a_room)
# songs_of = Album("Songs of Leonard Cohen", leonard_cohen, "Folk", 20.00, 12.00, "1967", 7, columbia)
# album_repository.save(songs_of)

# # Lizzo Album
# love_you = Album("Cuz I Love You", lizzo, "Soul/ Hip-Hop", 23.99, 14.39, "2019", 5, atlantic)
# album_repository.save(love_you)

# # Maggie Rogers Album
# past_life = Album("Heard it in a Past Life", maggie_rogers, "Folk Pop", 19.99, 11.99, "2019", 3, capitol)
# album_repository.save(past_life)


# # Paramore Albums
# after_laughter = Album("After Laughter", paramore, "Pop Rock", 17.99, 10.79, "2017", 4, fueled_by_ramen)
# album_repository.save(after_laughter)
# paramore_self_titled = Album("Paramore", paramore, "Pop Rock", 17.99, 10.79, "2013", 0, fueled_by_ramen)
# album_repository.save(paramore_self_titled)
# brand_new_eyes = Album("Brand New Eyes", paramore, "Pop Rock", 17.99, 10.79, "2009", 2, fueled_by_ramen)
# album_repository.save(brand_new_eyes)
# riot = Album("Riot!", paramore, "Alt-Rock", 17.99, 10.79, "2007", 1, fueled_by_ramen)
# album_repository.save(riot)
# falling = Album("All We Know is Falling", paramore, "Alt-Rock", 17.99, 10.79, "2005", 1, fueled_by_ramen)
# album_repository.save(falling)

# # Phoebe Bridgers Albums
# punisher = Album("Punisher", phoebe_bridgers, "Indie Rock", 21.99, 13.19, "2020", 6, dead_oceans)
# album_repository.save(punisher)
# stranger = Album("Stranger in the Alps", phoebe_bridgers, "Indie Rock", 21.99, 13.19, "2017", 5, dead_oceans)
# album_repository.save(stranger)

# # Sara Bareilles Albums
# chaos =  Album("Amidst the Chaos", sara, "Pop", 21.99, 13.19, "2019", 3, epic)
# album_repository.save(chaos)
# blessed_unrest = Album("The Blessed Unrest", sara, "Pop", 21.99, 13.19, "2013", 2, epic)
# album_repository.save(blessed_unrest)
# kaleidoscope = Album("Kaleidoscope Heart", sara, "Pop", 21.99, 13.19, "2010", 1, epic)
# album_repository.save(kaleidoscope)

# # Tallest Man on Earth Album

# fever_dream = Album("I Love You. It's a Fever Dream.", tallest_man, "Folk", 17.99, 10.79, "2019", 2, dead_oceans)
# album_repository.save(fever_dream)



pdb.set_trace()









