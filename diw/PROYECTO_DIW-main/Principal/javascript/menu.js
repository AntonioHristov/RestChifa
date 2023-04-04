var navegadorIcon = document.getElementById("listamenuIcon");
var navegador = document.getElementById("listamenu");
var navegadorList = document.querySelectorAll(".list");
var flag = 0;

navegadorIcon.onclick = function(){
        if(flag == 0){
            navegador.style.height="235px";
            navegadorIcon.style.height="30px";
            for(i=0; i<navegadorList.length; i++){
                navegadorList[i].style.display="block";
            }
            flag = 1;
        }else if(flag == 1){
            navegador.style.height="9%";
            navegadorIcon.style.height="100%";
            for(i=0; i<navegadorList.length; i++){
                navegadorList[i].style.display="none";
            }
            flag = 0;
        }
}