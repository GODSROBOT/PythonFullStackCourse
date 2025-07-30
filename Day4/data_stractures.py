# lets create lists for the top 10 Countrys for most populated
print("------------------------------------------------------------------------------")
print("              DATA STRUCTURES IN PYTHON                ")
print("------------------------------------------------------------------------------")

print("--------------------------------------------------------------------")
print("TYPE : LISTS")
print("Top 10 Most Populated Countries")
print("--------------------------------------------------------------------")
Top_10_populated_country = [
    "India",
    "China",
    "United States",
    "Indonasia",
    "Pakistan",
    "Nigeria",
    "Brazil",
    "Bangladesh",
    "Russia",
    "Mexico"
]
# Now lets use For loop for printing this lists
for i in Top_10_populated_country:
    print(i)
print("--------------------------------------------------------------------")
print("Top 10 Most Populated Countries (After Modification)")
print("--------------------------------------------------------------------")
# Now if we have to add new country to the list we have to use .append
Top_10_populated_country.append("Japan")
# Now if we have to remove a country from the list we can use .remove
# lets remove Mexico from the list
Top_10_populated_country.remove("Mexico")
# Now lets print the list again
for i in Top_10_populated_country:
    print(i)
# if we have to rearrange the lists we can use this method  
# Top_10_populated_country[1] = "India"
# Top_10_populated_country[0] = "China"
# Top_10_populated_country.insert(0, "Tokyo")  # if we want to insert a country at the start of the list

print("--------------------------------------------------------------------")
print("TYPE : TUPLES")
print("              Indian Prime Ministers                ")
print("--------------------------------------------------------------------")
# Now lets Have list of tuples for the top 10 Prime ministers of India
indian_prime_ministers = [
    ("Jawaharlal Nehru", 1947, 1964),
    ("Gulzarilal Nanda", 1964, 1964),      # Interim
    ("Lal Bahadur Shastri", 1964, 1966),
    ("Gulzarilal Nanda", 1966, 1966),      # Interim again
    ("Indira Gandhi", 1966, 1977),
    ("Morarji Desai", 1977, 1979),
    ("Charan Singh", 1979, 1980),
    ("Indira Gandhi", 1980, 1984),         # Second term
    ("Rajiv Gandhi", 1984, 1989),
    ("Vishwanath Pratap Singh", 1989, 1990),
    ("Chandra Shekhar", 1990, 1991),
    ("P. V. Narasimha Rao", 1991, 1996),
    ("Atal Bihari Vajpayee", 1996, 1996),  # Brief first term
    ("H. D. Deve Gowda", 1996, 1997),
    ("I. K. Gujral", 1997, 1998),
    ("Atal Bihari Vajpayee", 1998, 2004),  # Full second term
    ("Manmohan Singh", 2004, 2014),
    ("Narendra Modi", 2014, 2024)          # Ongoing (as of 2024)
]


for i in indian_prime_ministers:
    print(f"Prime Minister: {i[0]}, From: {i[1]} To: {i[2]}")
# Now lets add a new prime minister to the list
print("--------------------------------------------------------------------")
print("Simple Colour Sets")
print("--------------------------------------------------------------------")
Colour_sets = [
    ("Sky Blue", "#87CEEB"),
    ("Crimson", "#DC143C"),
    ("Neon Green", "#39FF14")
]
for i in Colour_sets:
    print(f"Colour: {i[0]}, hexcode: {i[1]}")

print("--------------------------------------------------------------------")
print("TYPE : DICTIONARIES")
print("              Movie Reviews and Ratings                ")
print("--------------------------------------------------------------------")
### Dictinories

# lets make a Move dictionary with there reviews and ratings
# lets Create them as each on there and then we can merge them
# Movie 
# Structured Movie Data
superman_2025 = {
    "🎬 Director": "James Gunn",
    "👨 Lead Actor": "David Corenswet",
    "👩 Lead Actress": "Rachel Brosnahan",
    "📝 PostTreak": "86% Positive, 74% Recommended",
    "🍅 Rotten Tomatoes": "83%",
    "📊 Metacritic": "68%",

    "👍 Pros": [
        "Hopeful, bright take on Superman",
        "Emotional immigrant storyline",
        "Nicholas Hoult's Lex Luthor performance praised",
        "George R.R. Martin called it 'Best of the year'"
    ],

    "👎 Cons": [
        "Too much CGI in the climax",
        "Rushed backstory pacing"
    ]
}

guardians_vol3_2023 = {
    "🎬 Director": "James Gunn",
    "👨 Lead Actor": "Chris Pratt as Star-Lord",
    "🦝 Rocket (Voice)": "Bradley Cooper",
    "🌱 Groot (Voice)": "Vin Diesel",
    "👩 Lead Actress": "Zoe Saldana as Gamora",
    "🤖 Notable Role": "Karen Gillan as Nebula",
    "📝 PostTreak": "92% Positive, 88% Recommended",
    "🍅 Rotten Tomatoes": "82%",
    "📊 Metacritic": "64%",

    "👍 Pros": [
        "Emotional arc for Rocket Raccoon",
        "Powerful soundtrack and music placement",
        "Best visual effects in the trilogy",
        "Strong group chemistry and humor"
    ],

    "👎 Cons": [
        "Pacing issues in mid-act",
        "Lacks major MCU stakes"
    ]
}

django_unchained_2012 = {
    "🎬 Director": "Quentin Tarantino",
    "👨 Lead Actor": "Jamie Foxx as Django",
    "🧠 Supporting Actor": "Christoph Waltz as Dr. King Schultz",
    "👿 Antagonist": "Leonardo DiCaprio as Calvin Candie",
    "👩 Lead Actress": "Kerry Washington as Broomhilda",
    "📝 PostTreak": "89% Positive, 85% Recommended",
    "🍅 Rotten Tomatoes": "87%",
    "📊 Metacritic": "81%",

    "👍 Pros": [
        "Brilliant performances, especially Waltz and DiCaprio",
        "Bold storytelling with sharp dialogue",
        "Visually stylish and emotionally gripping",
        "Tarantino's signature mix of violence and dark humor"
    ],

    "👎 Cons": [
        "Excessive graphic violence for some viewers",
        "Controversial use of racial language",
        "Slightly overlong runtime"
    ]
}

# Merged into one movie database
movies = {
    "superman 2025": superman_2025,
    "guardians of the galaxy vol. 3": guardians_vol3_2023,
    "django unchained": django_unchained_2012
}

# Search and display logic
movie = input("🎞️ Enter the movie name: ").strip().lower()
print("\n" + "=" * 50)

if movie in movies:
    print(f"🎬 Details for '{movie.title()}':\n")
    details = movies[movie]
    for key, value in details.items():
        if isinstance(value, list):
            print(f"{key}")
            for item in value:
                print(f"   • {item}")
        else:
            print(f"{key}: {value}")
else:
    print(f"❌ Movie '{movie.title()}' not found in the database.")

print("--------------------------------------------------------------------")
print("TYPE : SETS")
print("              Simple Sets                ")
print("--------------------------------------------------------------------")
# Sets data Structure
Numbers = {
    1,2,3,4,5,6,7,8,9,10,
    11,12,13,14,15,16,17,18,19,20,
    21,22,23,24,25,26,27,28,29,30,
    31,32,33,34,35,36,37,38,39,40,
    41,42,43,44,45,46,47,48,49,50,

    1,2,3,4,5,6,7,8,9,10,
    11,12,13,14,15,16,17,18,19,20,
    21,22,23,24,25,26,27,28,29,30,
    31,32,33,34,35,36,37,38,39,40,
    41,42,43,44,45,46,47,48,49,50
}

# Now lets print the set
print("Numbers in the set:")
for number in Numbers:
    print(f"{number}")