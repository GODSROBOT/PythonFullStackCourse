# 📘 Day 12 — HTML Wrap-up & Introduction to CSS

Welcome to **Day 12** of the Python Full Stack journey! 🚀
On this day, we **completed HTML basics** and moved into the world of **CSS (Cascading Style Sheets)** 🌈.
We explored **types of CSS** and applied them in a project showcasing the **Seven Ancient Wonders of the World** 🏛️.

---

## 🧑‍💻 Topics Covered

1. ✅ **Completion of HTML Basics**

   * Semantic structure
   * Sections, divs, headings, lists, and images

2. 🌈 **Introduction to CSS**

   * Purpose of CSS in styling web pages
   * Linking CSS with HTML

3. 🗂️ **Types of CSS**

   * **Inline CSS** → Directly inside the HTML element using the `style` attribute
   * **Internal CSS** → Defined within `<style>` tags in the HTML `<head>`
   * **External CSS** → Stored in a separate `.css` file and linked using `<link>`

---

## 🏛️ Project: Ancient Wonders of the World

We created a webpage to display the **Seven Wonders of the Ancient World** using a mix of **inline, internal, and external CSS**.

### 🔹 Key Features

* Dark background with highlighted text ✨
* Images styled with rounded borders 🖼️
* Inline transformations using `translate()` for positioning 🔄
* Flexbox usage to align and center content 📐

### 📄 Files

* `index.html` → HTML structure (with some inline & internal CSS)
* `style.css` → External stylesheet for global styling

---

## 📌 Code Snippets

### HTML Example (with inline CSS)

```html
<h1 style="color: rgb(255, 200, 0); font-family: Georgia; transform: translate(30%);">
    Ancient Wonders of the World
</h1>
```

### External CSS Example

```css
body {
    background-color: black;
    display: flex;
    align-items: center;
    justify-content: center;
}
img {
    height: 80px;
    width: 80px;
    border-radius: 20%;
    border: 2px solid rgb(255, 166, 0);
}
```

---

## 📝 Learnings & Takeaways

* **CSS = Webpage personality 👗** → HTML gives structure, CSS gives style.
* **Different CSS types** should be chosen wisely:

  * Inline: Quick fixes ⚡
  * Internal: Page-specific 🌟
  * External: Reusable across multiple pages 🌍
* Flexbox is a **powerful layout tool** for alignment.

---

## 🚀 Next Steps

In **Day 13**, we’ll continue with **CSS fundamentals**:

* Colors, gradients, and backgrounds
* Fonts and typography
* Box model (margin, border, padding, content)
* More on layouts (Flexbox & Grid)

---

✨ *Day 12 helped us bridge the gap between structure (HTML) and design (CSS).*

> **HTML builds the skeleton 🦴, CSS adds the style 🌈, and soon JavaScript will bring it to life ⚡.**
