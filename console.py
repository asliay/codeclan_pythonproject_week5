import pdb
from models.album import Album
from models.artist import Artist
from models.label import Label
from models.genre import Genre


import repositories.artist_repository as artist_repository
import repositories.label_repository as label_repository
import repositories.album_repository as album_repository
import repositories.genre_repository as genre_repository

# Clears data from tables
album_repository.delete_all()
label_repository.delete_all()
artist_repository.delete_all()
genre_repository.delete_all()

# ARTISTS - Populates Artists table
various = Artist("Various Artists")
artist_repository.save(various)
beyonce = Artist("Beyoncé")
artist_repository.save(beyonce)
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
janelle = Artist("Janelle Monáe")
artist_repository.save(janelle)
leonard_cohen = Artist("Leonard Cohen")
artist_repository.save(leonard_cohen)
lizzo = Artist("Lizzo")
artist_repository.save(lizzo)
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
dermot_kennedy = Artist("Dermot Kennedy")
artist_repository.save(dermot_kennedy)
rage = Artist("Rage Against the Machine")
artist_repository.save(rage)
paul_simon = Artist("Paul Simon")
artist_repository

# LABELS 
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
vertigo = Label("Vertigo")
label_repository.save(vertigo)
warner = Label("Warner Records")
label_repository.save(warner)
republic = Label("Republic Records")
label_repository.save(republic)


# GENRES
alt_rock = Genre("Alternative Rock")
genre_repository.save(alt_rock)

rock = Genre("Rock")
genre_repository.save(rock)

pop = Genre("Pop")
genre_repository.save(pop)

pop_rock = Genre("Pop Rock")
genre_repository.save(pop_rock)

soft_rock = Genre("Soft Rock")
genre_repository.save(soft_rock)

folk = Genre("Folk")
genre_repository.save(folk)

folk_pop = Genre("Folk Pop")
genre_repository.save(folk_pop)

folk_rock = Genre("Folk Rock")
genre_repository.save(folk_rock)

indie_rock = Genre("Indie Rock")
genre_repository.save(indie_rock)

soul_hop = Genre("Soul/ Hip-Hop")
genre_repository.save(soul_hop)

hip_hop = Genre("Hip Hop")
genre_repository.save(hip_hop)

rb = Genre("R&B")
genre_repository.save(rb)

funk = Genre("Funk")
genre_repository.save(funk)

rap_metal = Genre("Rap Metal")
genre_repository.save(rap_metal)


# ALBUMS - Populates Albums table


# Biffy Clyro Albums

endings = Album("A Celebration of Endings", biffy, alt_rock, 21.99, 14.99, "2020", "https://is5-ssl.mzstatic.com/image/thumb/Music114/v4/3a/e3/77/3ae37790-7982-c517-02b4-b4ea4b55a7b5/source/600x600bb.jpg", 4, fourteenth)
album_repository.save(endings)

ellipsis = Album("Ellipsis", biffy, alt_rock, 17.99, 11.99, "2016", "https://is2-ssl.mzstatic.com/image/thumb/Music49/v4/7b/29/cd/7b29cd44-0d47-963e-5ffe-89d67c6e7dc4/source/600x600bb.jpg", 5, fourteenth)
album_repository.save(ellipsis)

opposites = Album("Opposites", biffy, alt_rock, 20.99, 13.79, "2013", "https://is3-ssl.mzstatic.com/image/thumb/Music/v4/bc/b0/d7/bcb0d7a1-48f0-63d0-ea4b-a780e8f43dd6/source/600x600bb.jpg", 3, fourteenth)
album_repository.save(opposites)

revolutions = Album("Only Revolutions", biffy, alt_rock, 15.99, 9.99, "2009", "https://is2-ssl.mzstatic.com/image/thumb/Music/v4/d4/ba/68/d4ba6840-7a23-3e3e-eda4-ab39a00fbf30/source/600x600bb.jpg", 2, fourteenth)
album_repository.save(revolutions)

puzzle = Album("Puzzle", biffy, alt_rock, 25.99, 16.79, "2007", "https://is5-ssl.mzstatic.com/image/thumb/Music/v4/fb/27/17/fb2717b4-403d-9aa2-72ca-757849357e5a/source/600x600bb.jpg", 3, fourteenth)
album_repository.save(puzzle)

# # Dire Straits Albums
brothers = Album("Brothers in Arms", dire_straits, rock, 23.99, 15.59, "1985", "https://is4-ssl.mzstatic.com/image/thumb/Music118/v4/c5/1a/30/c51a303c-2f0a-197a-be89-903b302527b5/source/600x600bb.jpg", 1, vertigo)
album_repository.save(brothers)

making_movies = Album("Making Movies", dire_straits, rock, 22.99, 14.99, "1980", "https://is2-ssl.mzstatic.com/image/thumb/Music128/v4/d0/42/9e/d0429ee1-5338-c369-1aa2-b290ad655072/source/600x600bb.jpg", 2, vertigo)
album_repository.save(making_movies)

# # Fleetwood Mac Albums 
tango = Album("Tango in the Night", fleetwood_mac, pop_rock, 20.00, 12.00, "1987", "https://is3-ssl.mzstatic.com/image/thumb/Music111/v4/28/a6/a9/28a6a9f9-7040-37e3-cef9-ef6f8ecaabfa/source/600x600bb.jpg", 4, warner)
album_repository.save(tango)

mirage = Album("Mirage", fleetwood_mac, soft_rock, 18.00, 13.00, "1982", "https://is2-ssl.mzstatic.com/image/thumb/Music18/v4/30/5e/e2/305ee2d4-1520-4490-cd46-2336009989b1/source/600x600bb.jpg", 0, warner)
album_repository.save(mirage)

tusk = Album("Tusk", fleetwood_mac, rock, 20.00, 12.00, "1979", "https://is2-ssl.mzstatic.com/image/thumb/Music19/v4/2f/39/8d/2f398d29-996a-0800-6640-4d2e8680a30d/source/600x600bb.jpg", 2, warner)
album_repository.save(tusk)

rumours = Album("Rumours", fleetwood_mac, folk_rock, 19.00, 14.00, "1977", "https://is2-ssl.mzstatic.com/image/thumb/Music/v4/8e/75/28/8e752885-66d0-737c-11ef-4c706672997e/source/600x600bb.jpg", 5, warner)
album_repository.save(rumours)

fleetwood_self_titled = Album("Fleetwood Mac", fleetwood_mac, soft_rock, 23.99, 17.45, "1975", "https://cdn.shopify.com/s/files/1/2976/0132/products/3749712_540x.jpg?v=1598653825", 3, warner)
album_repository.save(fleetwood_self_titled)

# # Frightened Rabbit Albums
panic_attack = Album("Painting of a Panic Attack", frightened_rabbit, indie_rock, 21.99, 13.19, "2016", "https://is2-ssl.mzstatic.com/image/thumb/Music69/v4/a7/28/c5/a728c5a3-d583-e646-5eaa-0ad2b3b85d41/source/600x600bb.jpg", 6, atlantic)
album_repository.save(panic_attack)

pedestrian = Album("Pedestrian Verse", frightened_rabbit, indie_rock, 19.99, 11.99, "2013", "https://is1-ssl.mzstatic.com/image/thumb/Music/v4/fc/9e/24/fc9e2421-bc95-29cd-4fe4-d0d570c22c84/source/600x600bb.jpg", 1, atlantic)
album_repository.save(pedestrian)

midnight = Album("Midnight Organ Fight", frightened_rabbit, indie_rock, 22.99, 13.79, "2008", "https://is2-ssl.mzstatic.com/image/thumb/Music123/v4/53/79/37/53793762-eeef-8cce-96b2-6de1c18740e2/source/600x600bb.jpg", 0, fat_cat)
album_repository.save(midnight)

# # Hozier Albums
wasteland = Album("Wasteland, Baby!", hozier, folk_rock, 24.99, 14.99, "2019", "https://is4-ssl.mzstatic.com/image/thumb/Music114/v4/b8/61/a2/b861a286-5b7a-4827-b3e3-0875a8a554e2/source/600x600bb.jpg", 3, island)
album_repository.save(wasteland)

hozier_self_titled = Album("Hozier", hozier, folk_rock, 24.99, 14.99, "2014", "https://is5-ssl.mzstatic.com/image/thumb/Music118/v4/70/eb/5d/70eb5d85-7386-3d55-1d33-ac9400601a6b/source/600x600bb.jpg", 2, island)
album_repository.save(hozier_self_titled)


# # Janelle Monáe Album
dirty_computer = Album("Dirty Computer", janelle, funk, 21.99, 13.19, "2018", "https://is2-ssl.mzstatic.com/image/thumb/Music118/v4/f4/58/47/f4584702-bd77-52c3-f7e0-fa05f4e80397/source/600x600bb.jpg", 1, atlantic)
album_repository.save(dirty_computer)

# # Leonard Cohen Albums
thanks_for_the_dance = Album("Thanks for the Dance", leonard_cohen, folk_rock, 20.00, 12.00, "2019", "https://is5-ssl.mzstatic.com/image/thumb/Music123/v4/81/e4/7c/81e47c3d-596a-bb52-e44d-ed6d681fbec1/source/600x600bb.jpg", 5, columbia)
album_repository.save(thanks_for_the_dance)

darker = Album("You Want it Darker", leonard_cohen, folk_rock, 20.00, 12.00, "2016", "https://is3-ssl.mzstatic.com/image/thumb/Music62/v4/29/0f/e7/290fe7f2-3176-6300-3d3f-6d2946fb8fbf/source/600x600bb.jpg", 9, columbia)
album_repository.save(darker)

future = Album("The Future", leonard_cohen, soft_rock, 21.99, 14.19, "1992", "https://is2-ssl.mzstatic.com/image/thumb/Music1/v4/4e/54/5c/4e545cdc-b314-c38b-0839-0796cf70bcc3/source/600x600bb.jpg", 3, columbia)
album_repository.save(future)

your_man = Album("I'm Your Man", leonard_cohen, soft_rock, 19.99, 14.00, "1988", "https://is5-ssl.mzstatic.com/image/thumb/Music3/v4/47/03/7c/47037cbd-48ef-4a7a-d4aa-f43ce3e82135/source/600x600bb.jpg", 0, columbia)
album_repository.save(your_man)

various_positions = Album("Various Positions", leonard_cohen, folk, 20.00, 12.00, "1985", "https://is5-ssl.mzstatic.com/image/thumb/Music1/v4/8d/24/57/8d2457e3-882c-99e5-9ef4-fd29ce3bfc6b/source/600x600bb.jpg", 2, columbia)
album_repository.save(various_positions)

love_and_hate = Album("Songs of Love and Hate", leonard_cohen, folk, 17.99, 13.00, "1971", "https://is5-ssl.mzstatic.com/image/thumb/Music1/v4/d0/b4/66/d0b466ea-e5d3-9d27-8f88-3d4b4d101945/source/600x600bb.jpg", 8, columbia)
album_repository.save(love_and_hate)

from_a_room = Album("Songs from a Room", leonard_cohen, folk, 20.00, 12.00, "1969", "https://is5-ssl.mzstatic.com/image/thumb/Music3/v4/ac/b4/3e/acb43e0a-f83e-0268-d38d-f4b0da8cd373/source/600x600bb.jpg", 2,columbia)
album_repository.save(from_a_room)

songs_of = Album("Songs of Leonard Cohen", leonard_cohen, folk, 20.00, 12.00, "1967", "https://is3-ssl.mzstatic.com/image/thumb/Music5/v4/10/3a/c2/103ac256-eece-c5fc-5ce2-a0f800ec91e8/source/600x600bb.jpg", 7, columbia)
album_repository.save(songs_of)

# Lizzo Album
love_you = Album("Cuz I Love You", lizzo, soul_hop, 23.99, 14.39, "2019", "https://is3-ssl.mzstatic.com/image/thumb/Music123/v4/15/83/ad/1583adac-3f2e-050c-d5d6-6879a865cb5d/source/600x600bb.jpg", 5, atlantic)
album_repository.save(love_you)

# Maggie Rogers Album
past_life = Album("Heard it in a Past Life", maggie_rogers, folk_pop, 19.99, 11.99, "2019", "https://is5-ssl.mzstatic.com/image/thumb/Music128/v4/47/ec/46/47ec4695-ab8f-3be8-6ca5-5e4c2ba599b1/source/600x600bb.jpg", 3, capitol)
album_repository.save(past_life)


# Paramore Albums
after_laughter = Album("After Laughter", paramore, pop_rock, 17.99, 10.79, "2017", "https://is1-ssl.mzstatic.com/image/thumb/Music91/v4/b5/d7/94/b5d794e2-e67d-2be9-373e-6410c82437cc/source/600x600bb.jpg", 4, fueled_by_ramen)
album_repository.save(after_laughter)

paramore_self_titled = Album("Paramore", paramore, pop_rock, 17.99, 10.79, "2013", "https://is3-ssl.mzstatic.com/image/thumb/Music/v4/8b/45/51/8b4551f9-563c-57db-c611-a16f8574b181/source/600x600bb.jpg", 0, fueled_by_ramen)
album_repository.save(paramore_self_titled)

brand_new_eyes = Album("Brand New Eyes", paramore, pop_rock, 17.99, 10.79, "2009", "https://is3-ssl.mzstatic.com/image/thumb/Music62/v4/5d/db/33/5ddb3338-b808-ffee-4bd6-263b655a33ba/source/600x600bb.jpg", 2, fueled_by_ramen)
album_repository.save(brand_new_eyes)

riot = Album("Riot!", paramore, alt_rock, 17.99, 10.79, "2007", "https://is2-ssl.mzstatic.com/image/thumb/Music/v4/03/25/62/032562e5-4eed-2dce-46e8-6c5591aa30c7/source/600x600bb.jpg", 1, fueled_by_ramen)
album_repository.save(riot)

falling = Album("All We Know is Falling", paramore, alt_rock, 17.99, 10.79, "2005", "https://is5-ssl.mzstatic.com/image/thumb/Music/v4/f2/3e/8e/f23e8ea6-7071-090c-afeb-da363a0466a1/source/600x600bb.jpg", 1, fueled_by_ramen)
album_repository.save(falling)

# Phoebe Bridgers Albums
punisher = Album("Punisher", phoebe_bridgers, indie_rock, 21.99, 13.19, "2020", "https://is3-ssl.mzstatic.com/image/thumb/Music113/v4/55/5d/c8/555dc8e0-32f1-0a53-ad7a-422244d9f75e/source/600x600bb.jpg", 6, dead_oceans)
album_repository.save(punisher)

stranger = Album("Stranger in the Alps", phoebe_bridgers, indie_rock, 21.99, 13.19, "2017", "https://is4-ssl.mzstatic.com/image/thumb/Music127/v4/2b/58/db/2b58dbdc-4450-b270-946f-8fc0aa27b88f/source/600x600bb.jpg", 5, dead_oceans)
album_repository.save(stranger)

# Sara Bareilles Albums
chaos =  Album("Amidst the Chaos", sara, pop, 21.99, 13.19, "2019", "https://is2-ssl.mzstatic.com/image/thumb/Music114/v4/83/8a/0f/838a0f1b-84c0-377a-8823-bc49027ef9f3/source/600x600bb.jpg", 3, epic)
album_repository.save(chaos)

blessed_unrest = Album("The Blessed Unrest", sara, pop, 21.99, 13.19, "2013", "https://is3-ssl.mzstatic.com/image/thumb/Music118/v4/dd/9f/9d/dd9f9d3c-cce9-4378-6223-f1a5b92fdc55/source/600x600bb.jpg", 2, epic)
album_repository.save(blessed_unrest)

kaleidoscope = Album("Kaleidoscope Heart", sara, pop, 21.99, 13.19, "2010", "https://is2-ssl.mzstatic.com/image/thumb/Music128/v4/bc/2d/b0/bc2db0d9-6209-177b-80fc-afe38683b815/source/600x600bb.jpg", 1, epic)
album_repository.save(kaleidoscope)

# Tallest Man on Earth Album

fever_dream = Album("I Love You. It's a Fever Dream.", tallest_man, folk, 17.99, 10.79, "2019", "https://is5-ssl.mzstatic.com/image/thumb/Music113/v4/8f/3d/f9/8f3df9cf-b15d-883c-7cef-fe2b6c69de5a/source/600x600bb.jpg", 2, dead_oceans)
album_repository.save(fever_dream)

# Beyonce Albums

lemonade = Album("Lemonade", beyonce, rb, 21.99, 13.19, "2016", "https://is4-ssl.mzstatic.com/image/thumb/Music113/v4/50/a5/82/50a582f9-6690-ec06-14e7-e55d0d72e648/source/600x600bb.jpg", 3, columbia)
album_repository.save(lemonade)
beyonce_self_titled = Album("Beyoncé", beyonce, rb, 19.99, 11.99, "2013", "https://is2-ssl.mzstatic.com/image/thumb/Music6/v4/17/84/3a/17843a6d-1f2b-7e1e-a39f-3ff865110993/source/600x600bb.jpg", 4, columbia)
album_repository.save(beyonce_self_titled)

# Dermot Kennedy Album

without_fear = Album("Without Fear", dermot_kennedy, folk_pop, 19.99, 11.99, "2019", "https://is1-ssl.mzstatic.com/image/thumb/Music123/v4/72/26/4d/72264d37-4ae0-a1d2-73e3-e5e3413845fe/source/600x600bb.jpg", 1, island)
album_repository.save(without_fear)

# Spider-Verse soundtrack
spiderverse = Album("Spider-Man: Into the Spider-Verse", various, hip_hop, 19.99, 11.99, "2018", "https://is4-ssl.mzstatic.com/image/thumb/Music124/v4/36/9b/a2/369ba2e1-2dfc-6e2a-7065-4612af58fa0a/source/600x600bb.jpg", 2, republic)
album_repository.save(spiderverse)

# Rage Against the Machine album
rage_self_titled = Album("Rage Against the Machine", rage, rap_metal, 21.99, 13.19, "1992", "https://is3-ssl.mzstatic.com/image/thumb/Music113/v4/c8/2c/46/c82c46dc-eab8-4b62-1381-c2fae3d9b7a0/source/600x600bb.jpg", 1, epic)
album_repository.save(rage_self_titled)


pdb.set_trace()









