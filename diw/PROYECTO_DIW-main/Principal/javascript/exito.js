var num = document.getElementById("num");
var n =5;
window.setInterval(() => {
    num.innerHTML= n;
    n--;
}, 1100);

setTimeout(()=>{
    location.href="./index.php";
},7100)