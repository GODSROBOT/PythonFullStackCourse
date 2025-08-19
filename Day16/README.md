```js
<button id="Btn">Click Me</button>
<script>
document.getElementById("btn").addeventListner("Click", funtion()
{
    alert("Button clicked")
}
)
```
this will print after 2 second later but if we use setinterval
```js
<script>
console.log("Start");
setTimeout(() => {
    console.log("Runs after 2 seconds");
}, 2000);
console.log("End");
</script>
```
This will keepon print in each 2 second 
```js
<script>
console.log("Start");
setInterval(() => {
    console.log("Runs after 2 seconds");
}, 2000);
console.log("End");
</script>
```

json = java script obejct notion

Lets get async funtion
```js
async function getData()
{
    let response = await fetch ("")
}
```
Homework
1. Counter using click event
2. for mouseover we have to put image with using id and events : mouseover and mouseout
the image must change based in the mouseover and mouseout
3. for keydown : The event is Keydown , add eventlistner to the document.addEventListner
basicay the body colour should change basied in the KEY : R = Red ,G = Green , B = Blue 
if user press The R key in the keyboard they should be able get the body colur to the red and if b then Blue
and if green then green colour in the background 
4. 
```js
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
So we have to make it ours own celeberty and if possible we have put the images via api that we gave
!!!
5. using settimeout for our flag colour 
like every 3 second the body must change colour like orange , white and green 
6. for setinterval we have to print even and odd number printing in the console 