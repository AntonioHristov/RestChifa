let phone = document.getElementById("phone");

phone.addEventListener("input",function(){
    let value = phone.value;
        value = value.replace(/(\d{3})(\d{3})(\d{3})/,"$1-$2-$3");
        phone.value=value;
});