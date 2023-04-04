var phone = document.getElementById("phone");

phone.addEventListener("input",function(){
    let value = phone.value;
        value = value.replace(/(\d{3})(\d{3})(\d{3})/,"$1-$2-$3");
        phone.value=value;
});

var eye = document.getElementById('eyeIcon');
var passwd = document.getElementById("passw")
var flag = 0;
eye.onclick = function(){
    if(flag == 0 ){
        passwd.type = "text";
        this.src ="../IMG/IconSVG/eye-open-svgrepo-com.svg";
        flag = 1;
    }else if (flag == 1){
        passwd.type = "password";
        this.src ="../IMG/IconSVG/eye-closed-svgrepo-com.svg";
        flag = 0;
    }
}

