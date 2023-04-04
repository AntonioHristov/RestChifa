var numTarjeta = document.getElementById("numTarjeta");

numTarjeta.addEventListener("input",function(){
    let value = numTarjeta.value;
        value = value.replace(/(\d{4})(\d{4})(\d{4})(\d{4})/,"$1-$2-$3-$4");
        numTarjeta.value=value;
});