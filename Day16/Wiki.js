async function getData() {
    let response = await fetch("https://en.wikipedia.org/api/rest_v1/page/summary/Puneeth_Rajkumar")
    let data = await response.json();
    console.log(data);
}
getData();