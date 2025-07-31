# Lets create a sets of cards
cards = {
    "Hearts": {"Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"},
    "Diamonds": {"Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"},
    "Clubs": {"Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"},
    "Spades": {"Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"},
}

# Now lets print the cards
print("Cards in the deck:")
for suit, values in cards.items():
    print(f"{suit}: {', '.join(values)}")

# Lets create simple sets forms that will not reappear the same number twice
print("\nSimple Sets of Numbers:")
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
print("Numbers in the set:")
for number in Numbers:
    print(f"{number}")