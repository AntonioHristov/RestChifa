function no_img_on_error(obj_img = null) {
    if(obj_img != null)
    {
        obj_img.src = './../../static/restChifa/img/dishes/no_image.jpg';
    }
}

function reserveFormOnReset()
{
    var result = confirm('¿Quieres vacíar los datos de la reserva?');
    if(result)
    {
        document.getElementsByName("name_reserve_name")[0].setAttribute('value','');
        document.getElementsByName("name_reserve_prefix_tlf")[0].setAttribute('value','');
        document.getElementsByName("name_reserve_tlf")[0].setAttribute('value','');
        document.getElementsByName("name_reserve_date")[0].setAttribute('value','');
        document.getElementsByName("name_reserve_restaurant")[0].setAttribute('value','');
        document.getElementsByName("name_reserve_people")[0].setAttribute('value','');
        document.getElementsByName("name_reserve_email")[0].setAttribute('value','');
        document.getElementsByName("name_reserve_other")[0].innerHTML = "";
    }

    return result;
}

