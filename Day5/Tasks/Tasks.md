# 🧠 Day 5 – Data Structures Practice Tasks

---

## 🎯 Objective

Today you explored various built-in data structures in Python — Lists, Tuples, Dictionaries, and Sets — by creating your own real-world inspired tasks and solving them with creativity. This practice is key to becoming confident in problem solving with Python.

---

## 📁 Tasks Overview

Below are the custom-built tasks that you implemented. These reflect your independent understanding of how data structures can model real-world problems effectively.

---

### 🧾 1. Lists: Top Programming Languages

**Description:**

* A list of the **Top 10 most advanced programming languages** was created.
* The list was **updated** and **re-ordered** manually.

**Highlights:**

* Used `.append()` to add a new language.
* Used direct indexing to modify list elements.

```python
Languages = ["Rust", "Python", "TypeScript", ...]
Languages.append("JavaScript")
Languages[0] = "Python"
Languages[1] = "JavaScript"
```

---

### 📊 2. Dictionaries: Movie Rating System

**Description:**

* Created detailed dictionaries for 4 fictional/upcoming movies.
* Each dictionary included metadata (director, lead actors, ratings, pros, cons).
* Implemented a **selection system** using input to fetch specific movie info.

**Highlights:**

* Used nested dictionaries.
* Used lists inside dictionaries for pros & cons.
* Handled dictionary traversal using loops and conditionals.

```python
Movie_list = {
    "saiyaara": saiyaara_2025,
    "kingdom": kingdom_2025,
    ...
}
movie = input("Enter the movie name: ")
for key, value in Movie_list[movie].items():
    if isinstance(value, list):
        for item in value:
            print(item)
```

---

### 🔁 3. Tuples: Car Brands & Models

**Description:**

* Created a list of tuples where each tuple represents a car brand and its models.
* Used nested loops to print each brand with its respective models.

**Highlights:**

* Demonstrated how tuples can pair fixed keys (brands) with list values (models).
* Used `enumerate()` and `index()` effectively.

```python
car_brands = [
    ("BMW", ["X5", "X3"]),
    ("Tesla", ["Model S", "Model X"])
]
```

---

### ♠️ 4. Sets: Cards and Unique Numbers

**Description:**

* Modeled a **deck of cards** using nested sets.
* Demonstrated set uniqueness with repeated number input.

**Highlights:**

* Created a dictionary of suits, each containing a set of values.
* Used sets to automatically remove repeated numbers.

```python
cards = {
    "Hearts": {"Ace", "2", ..., "King"},
    ...
}
Numbers = {1, 2, 3, ..., 50, 1, 2, 3, ..., 50}
```

---

## ✅ What You Practiced

* ✔️ Data modeling with real-world context
* ✔️ Using correct methods for each data structure
* ✔️ Input/output control
* ✔️ Loops, conditionals, and formatting

---

## 🏁 Well Done!

You did this day completely by yourself — that's a huge milestone. Keep challenging yourself with creative tasks like these to sharpen your logic and Python fluency.

---

🔗 **Associated Files:**

* `lists.py`
* `tuples.py`
* `dictionary.py`
* `sets.py`
