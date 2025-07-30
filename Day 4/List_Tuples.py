# lets create lists for the top 10 Countrys for most populated

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
# for i in Top_10_populated_country:
#     print(i)

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

Colour_sets = [
    ("Sky Blue", "#87CEEB"),
    ("Crimson", "#DC143C"),
    ("Neon Green", "#39FF14")
]
for i in Colour_sets:
    print(f"Colour: {i[0]}, hexcode: {i[1]}")