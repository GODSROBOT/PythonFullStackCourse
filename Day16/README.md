# Day 16 – Events, Timing Functions & Async 🚀

Today we moved deeper into **JavaScript events, timing functions (`setTimeout`, `setInterval`) and async programming with `fetch`**.

---

## 🖱️ Event Listeners

We learned how to add event listeners to HTML elements.

```html
<button id="clickMeButton">ClickMe</button>
<script>
    document.getElementById("clickMeButton").addEventListener("click", function() {
        alert("Button clicked!");
    });
</script>
```

### Mouse Events Example

```html
<div id="message" style="border: 1px solid black; align-content: center;">check this</div>
<script>
    document.getElementById("message").addEventListener("mouseover", function() {
        this.style.color = "red";
        this.textContent = "Mouse over the message!";
        this.style.backgroundColor = "yellow";
    });
    document.getElementById("message").addEventListener("mouseout", function() {
        this.style.color = "black";
        this.textContent = "check this";
        this.style.backgroundColor = "white";
    });
</script>
```

### Keyboard Event Example

```html
<input type="text" id="inputField" placeholder="Type something...">
<script>
    document.getElementById("inputField").addEventListener("keydown", function() {
        console.log("Key pressed in input field, " + this.value);
    });
</script>
```

---

## ⏱️ Timing Functions

### `setTimeout`

Runs **once** after a delay.

```html
<script>
console.log("Start");
setTimeout(() => {
    console.log("Runs after 2 seconds");
}, 2000);
console.log("End");
</script>
```

### `setInterval`

Runs **repeatedly** at a given interval.

```html
<script>
console.log("Start");
setInterval(() => {
    console.log("Runs every 2 seconds");
}, 2000);
console.log("End");
</script>
```

---

## 🌐 Async & Fetch

We explored **async/await** for making API calls.

```js
async function getData() {
    let response = await fetch("https://en.wikipedia.org/api/rest_v1/page/summary/Puneeth_Rajkumar");
    let data = await response.json();
    console.log(data);
}
getData();
```

Another example that updates the DOM:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Wikipedia Fetch Activity</title>
</head>
<body>
  <h2>Wikipedia Summary 📖</h2>
  <div id="info"></div>

  <script>
    async function getData() {
      let response = await fetch("https://en.wikipedia.org/api/rest_v1/page/summary/Aamir_Khan");
      let data = await response.json();
      document.getElementById("info").innerHTML = `
        <h3>${data.title}</h3>
        <p>${data.extract}</p>
      `;
    }
    getData();
  </script>
</body>
</html>
```

---

## 🏡 Homework

1. **Counter using Click Event** → Button click should increase a counter on the page.
2. **Mouseover with Image Swap** → On `mouseover` and `mouseout`, swap an image.
3. **Keydown Events for Colors** → Change background color of the body based on key pressed:

   * `R` → Red
   * `G` → Green
   * `B` → Blue
4. **Wikipedia Fetch** → Choose your own celebrity, fetch data from Wikipedia API, and also display their image if available.
5. **setTimeout Flag Colors** → Change the background color every 3 seconds (Orange → White → Green).
6. **setInterval Even/Odd Printing** → Print even and odd numbers alternately in the console every 2 seconds.

### ✅ My Homework File
1. [Counter](/Day16/hw/Counter.html)
2. [Mouseover](/Day16/hw/Mouse.html)
3. [Keydown](/Day16/hw/RGB.html)
3. [Wikipedia](/Day16/hw/Wiki.html)
3. [setTimeout](/Day16/hw/Flagcolours.html)
3. [setInterval](/Day16/hw/even_odd.html)
---

✅ **Day 16 Summary**: Learned about **event handling**, **timing functions**, and **async/await**. Homework combines interactivity with async fetch requests.
