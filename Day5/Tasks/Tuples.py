# Lets create a list of tuples for car brands and their models
car_brands = [
    ("BMW", ["X5", "X3", "M3"]),
    ("Audi", ["A4", "Q5", "R8"]),
    ("Mercedes", ["C-Class", "E-Class", "S-Class"]),
    ("Tesla", ["Model S", "Model 3", "Model X"]),
    ("Ford", ["Mustang", "F-150", "Explorer"]),
]

# Lets print the car brands and their models
for index, (brand, models) in enumerate(car_brands, start=1):
    print(f"Car Brand: {brand}")
    print("Models:")
    for model in models:
        print(f"{models.index(model) + 1} - {model}")