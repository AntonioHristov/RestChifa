
/*function añadirCarrito(producto){ 
    //si existe la cookie significa que ya tiene un producto añadido por lo que concateno los productos 
    //anterirores con los nuevos
    //si no existe la crea
    if(comprobarCookie("producto")){

        var valorCookie = obtenerCookie("producto");
        var valorModificado = valorCookie+","+producto.name;
        document.cookie = "producto=" + valorModificado;
    }else{
        document.cookie = "producto=" + producto.name;
    }
}*/

//comprueba si existe una cookie con la clve que le pasamos que en este caso es producto
function comprobarCookie(clave) {
    var clave = obtenerCookie(clave);
    if (clave != "") {
        return true;
    } else {
        return false;
    }
}

//te devuelve el valor de la cookie que pasamos con la clave que en este caso sigue siendo producto al leerla sin
//esta funcion te devuelve producto='valor' por lo que tenemos que quitar la clave y el igual
function obtenerCookie(clave) {
    var name = clave + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') c = c.substring(1);
        //devuelve el valor una vez llegado al igual comprueba si el indice del igual es 0 y devuelve 
        if (c.indexOf(name) == 0) return c.substring(name.length, c.length);
    }
    return "";
}

function añadirCarrito(producto){ 
            $.ajax({

                method: "POST",
                url: "carrito.php",
                data: { nombre:producto }

            })

            .done(function( response ) {

                alert(response);

            });
}