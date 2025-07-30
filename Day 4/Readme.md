# 📘 Day 4 – Data Structures in Python

---

## 🔰 Topic Overview

Today's class focused on one of the most crucial foundations in Python – **Data Structures**. Understanding how to store, access, and manipulate data using built-in structures is key to writing efficient and readable code.

We covered:

- What are Data Structures?
- Why we need them in Python
- Four core built-in types:
  1. **Lists**
  2. **Tuples**
  3. **Dictionaries**
  4. **Sets**

---

## 🔸 1. Lists – `[]`

- Lists are **ordered**, **mutable**, and **allow duplicates**.
- They can store mixed data types.

### ✅ Example:
```python
grocery_list = ["Banana", "Milk", "Chicken"]
for item in grocery_list:
    print(item)
```

##  🔸 2. Tuples – `()`
- Tuples are ordered, immutable, and allow duplicates.
- Often used for fixed collections like RGB codes, coordinates, etc.
### ✅ Examples:
```py
colour_sets = (
    ("Sky Blue", "#87CEEB"),
    ("Crimson", "#DC143C"),
    ("Neon Green", "#39FF14")
)
for colour in colour_sets:
    print(f"Colour: {colour[0]}, hexcode: {colour[1]}")
```

## 🔸 3. Dictionaries – {}
- Dictionaries store data as key-value pairs.
- They are unordered, mutable, and don’t allow duplicate keys.
### ✅ Examples:
#### 1. Basic Dictionary
```py
student = {
    "name": "Arjun",
    "age": 21,
    "course": "AI & ML"
}
```
#### 2. Nested Dictionary
```py 
classroom = {
    "student1": {"name": "Priya", "marks": 85},
    "student2": {"name": "Rahul", "marks": 78},
    "student3": {"name": "Neha", "marks": 92}
}
```
#### 3. Using `dict()` Constructor
```py
person = dict(name="Ravi", age=30, city="Delhi")
```
#### 4. Phonebook Dictionary
```py
phonebook = {
    "Dad": "9876543210",
    "Mom": "9123456789",
    "Best Friend": "9988776655"
}
```
#### 5. Dictionary with List Values
```py 
shopping_cart = {
    "fruits": ["apple", "banana", "mango"],
    "vegetables": ["carrot", "beans"],
    "dairy": ["milk", "cheese"]
}
```
#### 6. Looping Through a Dictionary
```py 
for key, value in student.items():
    print(f"{key} : {value}")
```
#### 7. Adding / Updating / Deleting
```py 
student["age"] = 22         # Update
student["grade"] = "A+"     # Add
del student["course"]       # Delete
```

## 🔸 4. Sets – `{}`
- Sets are unordered, mutable, and do not allow duplicates.
- Ideal for storing unique values and doing mathematical operations.
### ✅ Examples:
#### Basic Set
```py 
fruits = {"apple", "banana", "mango"}
print(fruits)
``` 
#### Duplicate Removal
```py
numbers = {1, 2, 2, 3, 4, 4, 5}
print(numbers)
```
#### From List to Set
```py 
names = set(["Raj", "Priya", "Raj", "Simran"])
print(names)
```
#### Adding / Removing
```py
colors = {"red", "blue"}
colors.add("green")
colors.remove("blue")
colors.discard("yellow")  # Safe remove
```
#### Set Operations
```py
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))               # {1, 2, 3, 4, 5}
print(a.intersection(b))        # {3}
print(a.difference(b))          # {1, 2}
print(a.symmetric_difference(b))# {1, 2, 4, 5}
```

#### Looping & Membership
```py 
for item in fruits:
    print(item)

print("apple" in fruits)  # True
```
#### Empty Set
```py 
empty_set = set()
```
## 📝 Summary
## ✔️ Covered all 4 built-in data structures
## ✔️ Hands-on code examples for each
## ✔️ Set operations and dictionary nesting
## ✔️ Real-world mini tasks explored for each type
