# Lets create a lists for Top 10 Most advanced Langauges available 
Languages = [
    "Rust",
    "Python",
    "TypeScript",
    "Kotlin",
    "Go(Golang)",
    "Swift",
    "Julia",
    "Elixir",
    "Haskell",
    "Zig"
]
for i in Languages:
    print(f"{Languages.index(i) + 1}. {i}")
# lets update the list bt adding a new language
Languages.append("JavaScript")
# Lets try to rearrange the list a bit 
Languages[0] = "Python"
Languages[1] = "JavaScript"

print("\nUpdated List of Languages:")
for i in Languages:
    print(f"{Languages.index(i) + 1}. {i}")