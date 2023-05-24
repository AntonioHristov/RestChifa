function no_img_on_error(obj_img = null) {
    if(obj_img != null)
    {
        obj_img.src = './../../static/restChifa/img/dishes/no_image.jpg';
    }
}

function confirm_send()
{
    var is_valid = false;
    do
    {
        var response = prompt("¿Estas seguro que quieres reservar ahora? s/n");
        is_valid = (response == "s" || response == "n" || response == "si" || response == "no" || response == "y" || response == "yes");
        if(!is_valid)
        {
            alert("La respuesta recibida no es valida, las respuestas validas son 's' y 'n', que significan si y no.");
        }
    }while(!is_valid);

    if(!is_valid)
    {
        //Desactivar el evento de envio
    }
}

function confirm_reset()
{
    
}