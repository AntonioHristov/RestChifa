let recipido_registre = document.getElementById("Registre");
recipido_registre.addEventListener("click",function(e){
    let regist_passw = document.getElementById("regist_passw");
    let repit_regist_passw = document.getElementById("repit_regist_passw");
    let erro = document.getElementById("erro");
    if(regist_passw.value != repit_regist_passw.value){
        e.preventDefault();
        if(erro.textContent!= null){
            while(erro.firstChild){
                erro.removeChild(erro.firstChild);
            }
        }
        let erro_pasw = document.createElement("p");
        let text_erro = document.createTextNode("Error! Deben introducir dos contraseña igual!");
            erro_pasw.appendChild(text_erro);
            erro.style.color="red";
        regist_passw.style.backgroundColor="red";
        repit_regist_passw.style.backgroundColor="red";
            erro.appendChild(erro_pasw);
    }else{
        console.log("hola");
        regist_passw.style.backgroundColor="white";
        repit_regist_passw.style.backgroundColor="white";
        while(erro.firstChild){
            erro.removeChild(erro.firstChild);
        }
    }
})