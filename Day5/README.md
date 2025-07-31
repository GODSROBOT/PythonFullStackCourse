## Day 5 was Only practicales No theroy are new things to do so lets beign with excutng the program that we yesterday learned # 📘 Day 5 – Debugging & Mastering Python Data Structures

---

## 🔰 Overview

Welcome to **Day 5** of your Python learning journey!
This day focused on strengthening your grip on **Lists**, **Tuples**, **Dictionaries**, and **Sets** through practical **debugging exercises** and **hands-on tasks**.

You worked on identifying errors, correcting logic issues, and solving real-world Python problems with confidence.

---

## 📂 File Structure

```
Day5/
├── Debugging/
│   └── problems.md     # Real code bugs from each data structure
├── Tasks/
│   └── tasks.md        # Practice questions using loops + data structures
└── README.md           # This file
```

---

## 🧠 Concepts Covered

### ✅ Lists

* Appending vs indexing
* Handling out-of-range errors
* Reversing and summing digits

### ✅ Tuples

* Immutable structure handling
* Use in constant values or fixed-length records

### ✅ Dictionaries

* Updating and accessing safely
* Common mistakes with missing keys

### ✅ Sets

* Unordered nature
* Uniqueness enforcement
* Valid operations: union, intersection, difference

---

## 🐞 Debugging Examples

```python
numbers = (1, 2, 3)
numbers.append(4)  # ❌ Error: Tuples are immutable
```

✅ Fix:

```python
numbers = list(numbers)
numbers.append(4)
```

---

## 🤩 Practice Tasks

* ✅ Sum of digits using `while` loop
* ✅ Fibonacci series using `for` loop
* ✅ Factorial using `for` loop
* ✅ Count vowels in string using `for` loop
* ✅ GCD using `while` loop
* ✅ Reverse a number
* ✅ Find unique values using `set`

Each task uses **loops + data structures** to solve simple but foundational logic problems.

---

## 💡 Skills Sharpened

✔️ Syntax correction and logical error resolution
✔️ Confident use of core data structures
✔️ Reinforcement of control flow (loops)
✔️ Real-world debugging thought process

---

## 📌 Quick Tips

* Use `.append()` for lists, not `.add()`
* Access dictionary keys safely with `.get()`
* Remember: **Tuples are immutable**
* Sets do not support indexing
* Watch for indentation & type errors while looping

---

## 🔗 Resources

* Debugging Challenges: [`problems.md`](Day5/Debugging/problems.md)
* Practice Tasks: [`tasks.md`](Day5/Tasks/tasks.md)

---

## 🚀 Keep Going!

You're now better equipped to read, write, and **debug** Python code using the most important data structures. Day 6 will take this even further. Let's go! 💪
