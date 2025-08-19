# Day 17: Bootstrap Components

## 📘 Topics Covered

Today’s class was focused on **Bootstrap Components**, learning how to structure layouts and apply styles with Bootstrap utility classes.

### 📐 Width & Height Utilities

* `w-0`, `w-25`, `w-50`, `w-75`, `w-100` → Controls **width** percentage.
* `h-0`, `h-25`, `h-50`, `h-75`, `h-100` → Controls **height** percentage.

### 📊 Grid System (Columns)

* Columns are based on a **12-grid system**.
* Examples:

  * `col-6` → Takes **half width** (6/12).
  * `col-3` → Takes **quarter width** (3/12).
  * `col-8` → Takes **8/12 of the row**.
* You can mix and match columns as long as they sum to 12 (or fewer).

### 🃏 Bootstrap Cards

Bootstrap Cards allow you to create **structured content blocks**.

**Card Structure:**

```html
<div class="card">
  <div class="card-body">
    <h5 class="card-title">Card Title</h5>
    <p class="card-text">Some quick example text to build on the card title.</p>
  </div>
</div>
```

**Main Classes:**

* `card` → Wrapper for the card component.
* `card-body` → Contains card content.
* `card-title` → Title of the card.
* `card-text` → Regular text inside the card.

---

## 📝 Homework

### Task: **National Symbols of India Page**

1. Create a **Navbar** at the top.
2. Include 5 National Symbols with Bootstrap cards.

   * 🇮🇳 National Flag
   * 🦚 National Bird (Peacock)
   * 🐅 National Animal (Tiger)
   * 🌳 National Tree / Ganga as National River
   * 🪶 National Emblem (Lion Capital of Ashoka)

### ✅ My Homework File
[National Symbols of India](/Day18/Hw/India.html)
---
### Example Structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>National Symbols of India</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <!-- Navbar -->
  <nav class="navbar navbar-dark bg-dark">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">National Symbols of India</a>
    </div>
  </nav>

  <div class="container mt-4">
    <div class="row">
      <!-- Example Card -->
      <div class="col-4">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">National Flag</h5>
            <p class="card-text">The Tiranga is the national flag of India.</p>
          </div>
        </div>
      </div>
      <!-- Repeat for other symbols -->
    </div>
  </div>
</body>
</html>
```
