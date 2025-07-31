# Lets Create a dictionary for the movie reviews and ratings
saiyaara_2025 = {
    "🎬 Director": "Mohit Suri",
    "👨 Lead Actor": "Ahaan Panday",
    "👩 Lead Actress": "Aneet Padda",
    "📝 IMDb Rating": "7.1/10 (IMDb users) — a solid audience reception" ,
    "🍅 Rotten Tomatoes": "≈ 50% (partial reviews, mixed sentiment)" ,
    "📊 Metacritic": "n/a; IMDb user average suggests modest critical consensus",
    "📝 PostTreak": "≈ 75% audience positivity; noted as 2025’s third biggest Hindi hit ☑️",
    "👍 Pros": [
        "Chemistry of debut leads is refreshing",
        "Emotional storytelling backed by strong music",
        "High audience traction and box-office success"
    ],
    "👎 Cons": [
        "Critics flagged formulaic storyline",
        "Some viewers felt the writing lacked depth"
    ]
}

kingdom_2025 = {
    "🎬 Director": "Gowtam Tinnanuri",
    "👨 Lead Actor": "Vijay Deverakonda",
    "👩 Lead Actress": "Bhagyashri Borse",
    "📝 IMDb Rating": "Not yet listed publicly",
    "🍅 Rotten Tomatoes": "Not tracked formally",
    "📊 Metacritic": "n/a (early feedback focuses on visuals and performance)",
    "📝 PostTreak": "Mixed – praised for performance and visuals; criticized as derivative",
    "👍 Pros": [
    "Deverakonda’s intense, emotionally-driven lead display",
    "Stylish visuals & strong background score resonating with fans"
    ],
    "👎 Cons": [
    "Called ‘old wine in a new bottle’ by critics",
    "Criticism for uneven pacing and lack of narrative freshness"
    ]
}

mahavatar_narsimha_2025 = {
    "🎬 Director": "Ashwin Kumar", 
    "🎭 Voice Cast": "Aditya Raj Sharma, Haripriya Matta, Sanket Jaiswal (Hindi)",
    "📝 IMDb Rating": "≈ 8.5/10 (user reviews, independent ratings)",
    "🍅 Rotten Tomatoes": "Not listed yet",
    "📊 Metacritic": "n/a (no critic aggregate yet)",
    "📝 PostTreak": "Highly positive on social media; praised as culturally resonant",
    "👍 Pros": [
    "Visually stunning and technically polished animation",
    "Authentic mythological storytelling connecting with audiences",
    "Deep emotional impact for family viewers"
    ],
    "👎 Cons": [
    "Minor pacing issues noted in quieter segments",
    "Emotional depth uneven in non-action scenes"
    ]
}

jurassic_world_rebirth_2025 = {
    "🎬 Director": "Gareth Edwards",
    "👨 Lead Actor": "Scarlett Johansson as Zora Bennett",
    "👨 Supporting": "Mahershala Ali as Duncan Kincaid; Jonathan Bailey as Dr. Henry Loomis",
    "📝 IMDb Rating": "Not confirmed yet",
    "🍅 Rotten Tomatoes": "≈ 60% (critic consensus: entertaining yet unoriginal)",
    "📊 Metacritic": "~3/5 average (mixed reviews cited)",
    "📝 PostTreak": "Mixed – nostalgic visuals and action praised; story seen as repetitive",
    "👍 Pros": [
    "Strong franchise nostalgia and exciting set pieces",
    "Solid ensemble chemistry with high production value"
    ],
    "👎 Cons": [
    "Predictable plot reliant on franchise tropes",
    "Underdeveloped characters and lack of narrative innovation"
    ]
}

Movie_list = {
    "saiyaara": saiyaara_2025,
    "kingdom": kingdom_2025,
    "mahavatar narsimha": mahavatar_narsimha_2025,
    "jurassic world rebirth": jurassic_world_rebirth_2025
}
# print(f"Movies available = {Movie_list}")
print("""
Movies available : 
1. Saiyaara
2. Kingdom
3. Mahavatar Narsimha
4. Jurassic World Rebirth
""")
movie = input("🎞️  Enter the movie name: ").strip().lower()
details = Movie_list[movie]
if movie == "saiyaara" :
    details = Movie_list[movie]
    for key, value in details.items():
        if isinstance(value, list):
            print(f"{key}")
            for item in value:
                print(f"   • {item}")
        else:
            print(f"{key}: {value}")
elif movie == "kingdom" :
    details = Movie_list[movie]
    for key, value in details.items():
        if isinstance(value, list):
            print(f"{key}")
            for item in value:
                print(f"   • {item}")
        else:
            print(f"{key}: {value}")
elif movie == "mahavatar narsimha" :
    details = Movie_list[movie]
    for key, value in details.items():
        if isinstance(value, list):
            print(f"{key}")
            for item in value:
                print(f"   • {item}")
        else:
            print(f"{key}: {value}")
elif movie == "jurassic world rebirth":
        details = Movie_list[movie]
        for key, value in details.items():
            if isinstance(value, list):
                print(f"{key}")
                for item in value:
                    print(f"   • {item}")
        else:
            print(f"{key}: {value}")