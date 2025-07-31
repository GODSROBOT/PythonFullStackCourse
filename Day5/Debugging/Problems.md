# 🚧 Debugging Practice – Python Data Structures

This document contains structured problems to enhance your problem-solving skills using Python's core data structures. Each problem demonstrates common beginner-level mistakes related to **Lists**, **Tuples**, **Dictionaries**, **Sets**, and **Mixed Types**.

---

## 🔢 1. List Debugging: Index Errors & Operations

### 🧬 Problem:

You're trying to access an index that doesn’t exist and modify a list item.

```python
fruits = ["apple", "banana", "orange"]
fruits.append("grape")
fruits[3] = "melon"
print(fruits[4])
```

### 🧠 What to Learn:

* How `append()` affects indexing
* What happens when accessing out-of-range indexes
* Proper way to replace an item

---

## 🖇️ 2. Tuple Debugging: Immutability

### 🧬 Problem:

Trying to modify a tuple, which is not allowed.

```python
student_info = ("John", 16, "Grade 10")
student_info[1] = 17
print("Updated Age:", student_info[1])
```

### 🧠 What to Learn:

* Tuples are immutable
* How to work with tuples if you need changes (hint: convert to list)

---

## 🔑 3. Dictionary Debugging: Key Errors & Incorrect Add Method

### 🧬 Problem:

Accessing a non-existent key and misusing `append()` on a dictionary.

```python
grades = {"Alice": 85, "Bob": 92}
print("Charlie’s grade is", grades["Charlie"])
grades["Alice"] = 88
grades.append("Eve": 90)
```

### 🧠 What to Learn:

* How to handle missing keys safely (`get()` or `in`)
* Adding new entries properly (`grades["Eve"] = 90`)

---

## 🎨 4. Set Debugging: No Indexing & Hashable Elements

### 🧬 Problem:

Trying to access sets using index and adding unhashable elements.

```python
colors = {"red", "blue", "green"}
colors[1] = "yellow"
colors.add(["black", "white"])
print(colors)
```

### 🧠 What to Learn:

* Sets do not support indexing
* Only hashable (immutable) types can be added (e.g., strings, tuples)

---

## 🔁 5. Mixed Debugging: Type-Specific Operations

### 🧬 Problem:

Applying a list method to a set and accessing keys that don’t exist.

```python
students = ["Alice", "Bob", "Charlie"]
ages = {"Alice": 15, "Bob": 16}
unique_names = set(students)
unique_names.add("Alice")
students.add("Daniel")
print(ages["Charlie"])
```

### 🧠 What to Learn:

* `.add()` doesn't work on lists, use `.append()`
* `KeyError` when accessing missing dictionary keys

---

📚 **Next Steps:**
Try fixing each bug and re-run the corrected code. Make sure you understand:

* Data type behavior
* Safe data access
* Proper method usage

---
# ✅ Day 5 – Python Debugging Tasks

---

## 🔧 TASK 1: List Debugging – Index Errors & Operations

### ❓ Problem:

```python
fruits = ["apple", "banana", "orange"]
fruits.append("grape")
fruits[3] = "melon"
print(fruits[4])
```

### 🛠️ Bug Description:

* `fruits[3] = "melon"` is fine as it replaces "grape".
* But `print(fruits[4])` throws `IndexError` since there's no 5th element.

### ✅ Corrected:

```python
fruits = ["apple", "banana", "orange"]
fruits.append("grape")
fruits[3] = "melon"
print(fruits)
```

---

## 🔧 TASK 2: Tuple Debugging – Immutability

### ❓ Problem:

```python
student_info = ("John", 16, "Grade 10")
student_info[1] = 17
print("Updated Age:", student_info[1])
```

### 🛠️ Bug Description:

* Tuples are immutable. You can't change `student_info[1]`.

### ✅ Corrected:

```python
student_info = ("John", 17, "Grade 10")
print("Updated Age:", student_info[1])
```

---

## 🔧 TASK 3: Dictionary Debugging – Key Errors & Adding Elements

### ❓ Problem:

```python
grades = {"Alice": 85, "Bob": 92}
print("Charlie’s grade is", grades["Charlie"])
grades["Alice"] = 88
grades.append("Eve": 90)
```

### 🛠️ Bug Description:

* `grades["Charlie"]` raises `KeyError`.
* `.append()` doesn't work with dictionaries.

### ✅ Corrected:

```python
grades = {"Alice": 85, "Bob": 92}
print("Charlie’s grade is", grades.get("Charlie", "Not Found"))
grades["Alice"] = 88
grades["Eve"] = 90
```

---

## 🔧 TASK 4: Set Debugging – No Indexing & Hashable Elements

### ❓ Problem:

```python
colors = {"red", "blue", "green"}
colors[1] = "yellow"
colors.add(["black", "white"])
print(colors)
```

### 🛠️ Bug Description:

* Sets don't support indexing like `colors[1]`.
* `.add()` can only take hashable (immutable) items, not a list.

### ✅ Corrected:

```python
colors = {"red", "blue", "green"}
colors.add("yellow")
colors.update(["black", "white"])
print(colors)
```

---

## 🔧 TASK 5: Mixed Debugging – Type-Specific Operations

### ❓ Problem:

```python
students = ["Alice", "Bob", "Charlie"]
ages = {"Alice": 15, "Bob": 16}
unique_names = set(students)
unique_names.add("Alice")
students.add("Daniel")
print(ages["Charlie"])
```

### 🛠️ Bug Description:

* `students` is a list; you can't use `.add()`, use `.append()` instead.
* `ages["Charlie"]` causes `KeyError`.

### ✅ Corrected:

```python
students = ["Alice", "Bob", "Charlie"]
ages = {"Alice": 15, "Bob": 16}
unique_names = set(students)
unique_names.add("Alice")
students.append("Daniel")
print(ages.get("Charlie", "Not Found"))
```
