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
        regist_passw.style.backgroundColor="white";
        repit_regist_passw.style.backgroundColor="white";
        while(erro.firstChild){
            erro.removeChild(erro.firstChild);
        }
    }
})

var eye1 = document.getElementById('eyeIconR1');
var eye2 = document.getElementById('eyeIconR2');
var Rpasswd1 = document.getElementById("Rpasswd1")
var Rpasswd2 = document.getElementById("Rpasswd2")
var flag = 0;
eye1.onclick = function(){
    if(flag == 0 ){
        Rpasswd1.type = "text";
        this.src ="../IMG/IconSVG/eye-open-svgrepo-com.svg";
        flag = 1;
    }else if (flag == 1){
        Rpasswd1.type = "password";
        this.src ="../IMG/IconSVG/eye-closed-svgrepo-com.svg";
        flag = 0;
    }
}

eye2.onclick = function(){
    if(flag == 0 ){
        Rpasswd2.type = "text";
        this.src ="../IMG/IconSVG/eye-open-svgrepo-com.svg";
        flag = 1;
    }else if (flag == 1){
        Rpasswd2.type = "password";
        this.src ="../IMG/IconSVG/eye-closed-svgrepo-com.svg";
        flag = 0;
    }
}