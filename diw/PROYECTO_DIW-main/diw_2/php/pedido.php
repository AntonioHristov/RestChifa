<?php
require("src/init.php");

//$nombreUsuario viene dado por la sesion al logearte

$DB->ejecuta("SELECT * from pedido WHERE nombre = ?", $nombreUsuario);

$datos = $DB->obtenDatos();

array_walk($datos,function($element, $clave){
    array_walk($element,function($element, $clave){
            
        if($clave == "nombre"){
            $nombre = $element;
        }
        if($clave == "cantidad"){
            echo "<p class='descripcion'>" . $element . "</p>";
        }
        if($clave == "producto"){
            echo "<h4 class='precio'>" . $element . "</h4>";
        }
        if($clave == "nombreProducto"){
            echo "<h4 class='precio'>" . $element . "</h4>";
        }

    });
});
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div>
        <h4>Hola, <?= $nombreUsuario ?>  su pedido es el siguiente</h4>
        <p></p>
    </div>
</body>
</html>