# 📘 Day 16 – Bootstrap Introduction

---

## 🎯 Objective

Day 16 was focused on learning **Bootstrap**, a powerful front-end framework that makes it easier to design responsive, mobile-first websites. We explored its **grid system, components, and utilities**.

--- 
## 🌐 Official Documentation

* [Bootstrap 5 Docs](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
* [Bootstrap Examples](https://getbootstrap.com/docs/5.3/examples/)
* [Bootstrap Components](https://getbootstrap.com/docs/5.3/components/alerts/)
* [Bootstrap Layout & Grid](https://getbootstrap.com/docs/5.3/layout/grid/)
* [Bootstrap Utilities](https://getbootstrap.com/docs/5.3/utilities/api/)

---

## 📚 Topics Covered

### 1. 🌐 What is Bootstrap?

* Bootstrap is an **open-source CSS framework**.
* Helps in designing **responsive websites quickly**.
* Includes **CSS + JavaScript** components.
* Eliminates the need to write custom CSS for many repetitive styles.

### 2. 🏗️ Bootstrap Grid System

* Based on **12-column layout**.
* Supports **responsive breakpoints**:

  * `xs` → Extra small devices (mobile)
  * `sm` → Small devices (tablet)
  * `md` → Medium devices (desktop)
  * `lg` → Large devices (larger desktops)
  * `xl` → Extra-large screens
* Example:

  ```html
  <div class="row">
    <div class="col-md-6">Left Column</div>
    <div class="col-md-6">Right Column</div>
  </div>
  ```

### 3. 🎨 Bootstrap Components

* **Navbar** → Responsive navigation bar.
* **Cards** → Pre-styled content containers.
* **Buttons** → `btn btn-primary`, `btn btn-success` etc.
* **Forms** → Easy styling of input fields, labels, and checkboxes.
* **Modals** → Pop-up dialog boxes.

### 4. ⚡ Bootstrap Utilities

* **Spacing** → `m-3` (margin), `p-2` (padding).
* **Text** → `text-center`, `text-uppercase`.
* **Colors** → `bg-primary`, `text-danger`.
* **Flexbox utilities** → `d-flex`, `justify-content-between`.

---

## 🔗 Adding Bootstrap to Your Project


## 🚀 Importing Bootstrap with CDN (No Installation Needed)

Add this in your `<head>` section:

```html
<!-- Bootstrap CSS -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">

<!-- Bootstrap JS Bundle (with Popper) -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
```

---

## 🔹 Basic Bootstrap Examples

### ✅ Buttons

```html
<button class="btn btn-primary">Primary</button>
<button class="btn btn-success">Success</button>
<button class="btn btn-danger">Danger</button>
```

### ✅ Grid Layout

```html
<div class="container">
  <div class="row">
    <div class="col bg-primary text-white">Column 1</div>
    <div class="col bg-secondary text-white">Column 2</div>
    <div class="col bg-success text-white">Column 3</div>
  </div>
</div>
```

### ✅ Navbar

```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">MySite</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item"><a class="nav-link active" href="#">Home</a></li>
        <li class="nav-item"><a class="nav-link" href="#">About</a></li>
        <li class="nav-item"><a class="nav-link" href="#">Contact</a></li>
      </ul>
    </div>
  </div>
</nav>
```

### ✅ Card Component

```html
<div class="card" style="width: 18rem;">
  <img src="https://via.placeholder.com/150" class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">Card Title</h5>
    <p class="card-text">This is a simple card with some text and a button.</p>
    <a href="#" class="btn btn-primary">Read More</a>
  </div>
</div>
```

---

## ✅ Summary

* Learned what **Bootstrap** is.
* Understood the **grid system**.
* Explored **components and utilities**.
* Practiced **CDN integration**.
* Homework: Build a **Bootstrap mini-website**.

🚀 This sets the foundation for building **modern, responsive websites faster**!
