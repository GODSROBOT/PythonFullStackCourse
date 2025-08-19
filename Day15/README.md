# Day 15 – JavaScript Control Flow & DOM 🎯

Today’s class was rushed because the lecture was moving fast, so I made quick notes. Let’s make them more structured and detailed.

---

## 📚 Topics Covered

### 1. Writing Simple JS Scripts

* **Even/Odd Numbers** – Check if a number is even or odd.
* **Array of Numbers** – Iterate through an array.
* **Divisible by 5** – Print numbers divisible by 5.

---

### 2. DOM Manipulation

We started learning how to select and edit HTML elements using JavaScript.

#### Old Way:

```js
const myHeading = document.getElementById("Heading");
myHeading.textContent = "Manvith";
myHeading.style.color = "white";
```

#### Modern Way (Preferred):

```js
const myHeading = document.querySelector("#Heading");
myHeading.textContent = "Manvith";
myHeading.style.color = "white";
```

⚡ `getElementById` still works but **`querySelector`** is now the industry standard because it’s more flexible (can select by id, class, tag, etc.).

---

## 🏗️ Control Flow & DOM in Practice

* **Control Flow** helps us run conditions (if/else, loops) to decide how scripts behave.
* **DOM (Document Object Model)** lets us interact with and change HTML elements using JavaScript.

Example:

```js
for (let i = 1; i <= 20; i++) {
    if (i % 2 === 0) {
        console.log(i + " is Even");
    } else {
        console.log(i + " is Odd");
    }
}
```
---

## 📝 Homework

We had to:

1. Create a heading named **Java** in HTML.
2. Select the element and change it to **JavaScript**.
3. Apply some styling.
4. Add Java information.
5. Then remove that Java info and add **JavaScript** info using **createElement**.

### ✅ My Homework File
[Homework](/Day15/Homework/hw.html)
---
## 📂 Folder Structure

```
Day15/
│
├── controlflow/     # Notes & practice files for control flow (if-else, loops, switch)
│
├── DOM/             # Notes & practice files for Document Object Model manipulations
│
├── Homework/        # Assigned exercises and completed solutions
│
└── README.md        # Summary of Day 15 learning and tasks
```