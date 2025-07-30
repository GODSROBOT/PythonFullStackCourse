# 📘 Day 4 – Data Structures in Python

---

## 🔰 Topic Overview

Today's class focused on one of the most crucial foundations in Python – **Data Structures**. Understanding how to store, access, and manipulate data using built-in structures is key to writing efficient and readable code.

We covered:

* What are Data Structures?
* Why we need them in Python
* Four core built-in types:

  1. **Lists**
  2. **Tuples**
  3. **Dictionaries**
  4. **Sets**

---

## 🔗 File Link

**Python Code:** [`data_structures.py`](./data_structures.py)

---

## 🔸 1. Lists – `[]`

* Lists are **ordered**, **mutable**, and **allow duplicates**.
* They can store mixed data types.

### ✅ Example:

```python
grocery_list = ["Banana", "Milk", "Chicken"]
for item in grocery_list:
    print(item)
```

### ✅ Real World Example:

```python
Top_10_populated_country = ["India", "China", "United States", "Indonesia", "Pakistan"]
Top_10_populated_country.append("Japan")  # Add
Top_10_populated_country.remove("Mexico")  # Remove
```

---

## 🔸 2. Tuples – `()`

* Tuples are ordered, immutable, and allow duplicates.
* Often used for fixed collections like RGB codes, coordinates, etc.

### ✅ Examples:

```python
colour_sets = (
    ("Sky Blue", "#87CEEB"),
    ("Crimson", "#DC143C"),
    ("Neon Green", "#39FF14")
)
for colour in colour_sets:
    print(f"Colour: {colour[0]}, hexcode: {colour[1]}")
```

### ✅ Prime Minister Records:

```python
indian_prime_ministers = [
    ("Jawaharlal Nehru", 1947, 1964),
    ("Narendra Modi", 2014, 2024)
]
```

---

## 🔸 3. Dictionaries – `{}`

* Dictionaries store data as key-value pairs.
* They are unordered, mutable, and don’t allow duplicate keys.

### ✅ Examples:

```python
student = {
    "name": "Arjun",
    "age": 21,
    "course": "AI & ML"
}
```

### ✅ Nested Movie Reviews:

```python
movies = {
    "superman 2025": {
        "Director": "James Gunn",
        "Lead Actor": "David Corenswet"
    }
}
```

### ✅ Looping & Updating:

```python
for key, value in student.items():
    print(f"{key} : {value}")

student["grade"] = "A+"  # Add
```

---

## 🔸 4. Sets – `{}`

* Sets are unordered, mutable, and do not allow duplicates.
* Ideal for storing unique values and doing mathematical operations.

### ✅ Examples:

```python
fruits = {"apple", "banana", "mango"}
fruits.add("grape")
fruits.remove("banana")
```

### ✅ Use Case:

```python
numbers = set([1, 2, 2, 3, 4, 4, 5])
print(numbers)  # duplicates removed
```

### ✅ Set Operations:

```python
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))
print(a.intersection(b))
```

---

## 📝 Summary

### ✔️ Covered all 4 built-in data structures

### ✔️ Hands-on code examples for each

### ✔️ Set operations and dictionary nesting

### ✔️ Real-world mini tasks explored for each type

---

🔗 **Source Code File:** [`data_structures.py`](./data_structures.py)
