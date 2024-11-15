def popular_destinations():
    print("-"*140)
    print(
        """Popular Destinations in Ladakh!

1. Pangong Lake: A mesmerizing lake known for its ever-changing hues, as featured in the Bollywood movie '3 Idiots.'"
2. Nubra Valley: The 'Valley of Flowers' offers breathtaking landscapes and the unique experience of riding double-humped camels.
3. Tso Moriri Lake: A serene high-altitude lake that reflects the surrounding mountains like a mirror.
4. Magnetic Hill: A mysterious spot where vehicles appear to move uphill against gravity.
5. Leh Palace: Explore the ancient royal residence and enjoy panoramic views of Leh town."""
    )
    print("-"*140)

def traditional_cuisine():
    print("-"*140)
    print("""Traditional Food of Ladakh!

1. Momos: Delicious dumplings filled with savory meat or vegetables, served with spicy dipping sauce."
2. Thukpa: A soul-warming noodle soup with vegetables and choice of meat, perfect for Ladakh's chilly weather."
3. Skyu: A hearty stew made with wheat flour noodles, vegetables, and mutton, a traditional Ladakhi staple."
4. Chhupri: A mouthwatering dessert made from dried apricots, offering a sweet delight."
5. Paba: A unique Ladakhi bread, made from roasted barley flour and butter, served with butter tea."""
    )
    print("-"*140)

def adventure_activities():
    print("-"*140)
    print("""Adventure Activities in Ladakh!

1. Trekking: Embark on thrilling treks like Markha Valley or Stok Kangri to witness stunning landscapes and test your endurance.
2. River Rafting: Navigate the exhilarating rapids of the Zanskar and Indus rivers for an adrenaline-pumping experience.
3. Biking: Ride through the majestic landscapes on Leh-Manali Highway, a dream route for biking enthusiasts.
4. Camel Safari: Take a unique camel safari in the cold deserts of Nubra Valley, a memorable way to explore the region.
5. Wildlife Safari: Experience Ladakh's diverse wildlife at Hemis National Park, home to snow leopards, ibex, and more."""
    )
    print("-"*140)

def festivals_and_culture():
    print("-"*140)
    print("""Festivals and Culture of Ladakh!

1. Hemis Festival: Ladakh's biggest and most vibrant festival, celebrating the birth anniversary of Guru Padmasambhava.
2. Losar: The Ladakhi New Year, marked by colorful celebrations, dance performances, and traditional rituals.
3. Ladakhi Wedding: Witness the unique customs and rituals of a traditional Ladakhi wedding.
4. Archery Contest: Enjoy the thrilling traditional sport of archery, which is an integral part of Ladakh's culture.
5. Dosmoche: The 'Festival of Scapegoat,' celebrated with masked dances and rituals to drive away evil spirits."""
    )
    print("-"*140)

def local_handicrafts():
    print("-"*140)
    print("""Local Handicrafts of Ladakh!

1. Pashmina Shawls: Luxurious, fine wool shawls made from the softest undercoat of Himalayan goats.
2. Thangka Paintings: Intricately detailed paintings depicting Buddhist deities and symbols.
3. Prayer Wheels: Wooden or metal wheels inscribed with sacred mantras, believed to bring blessings when spun.
4. Apricot Oil: Pure and aromatic oil extracted from apricot kernels, used for skincare and massage.
5. Woolen Carpets: Handwoven carpets with vibrant colors and traditional patterns, adding warmth to any space."""
    )
    print("-"*140)


print("-"*140)
print(
    """Welcome to Ladakh Tourism Information Bureau!

Ladakh, often referred to as "The Land of High Passes," is a breathtakingly beautiful region in the northern part of India, 
characterized by its rugged mountainous terrain, pristine lakes, ancient monasteries, and a vibrant blend of Tibetan and Indian cultures."""
)
print("-"*140)

while True:
    print("""Feel free to make a selection:

1. Popular Destinations
2. Traditional Cuisine
3. Adventure Activities
4. Festivals and Cultures
5. Local Handicrafts
6. Exit""")
    print("-"*140)

    user = int(input("Enter (1-5): "))

    if user == 1:
        popular_destinations()
    
    elif user == 2:
        traditional_cuisine()

    elif user == 3:
        adventure_activities()

    elif user == 4:
        festivals_and_culture()

    elif user == 5:
        local_handicrafts()

    elif user == 6:
        print("-"*140)
        print("Thank you for exploring Ladakh with us! Have a great day!")
        print("-"*140)
        break
    
    else:
        print("-"*140)
        print("Invalid Input")
        print("-"*140)