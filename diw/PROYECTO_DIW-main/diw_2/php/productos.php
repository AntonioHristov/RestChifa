<?php

require("./src/init.php");

if(isset($_GET['nombreProductos'])){
    $nombreProductos = $_GET['nombreProductos'];
}

function pintarProductos($nombreProductos, $DB){

    $DB->ejecuta("SELECT * from $nombreProductos");

    $datos = $DB->obtenDatos();

    $array_total = array_map(function ($element){
        return $element;
        /*array_walk($element,function($element, $clave){
            //echo "$clave . $element <br> \n";
            return $element;
        });*/
    }, $datos);

    print_r($array_total);

    /*echo "<!DOCTYPE html>
            <html lang='en'>
            <head>
                <meta charset='UTF-8'>
                <meta http-equiv='X-UA-Compatible' content='IE=edge'>
                <meta name='viewport' content='width=device-width, initial-scale=1.0'>
                <link rel='stylesheet' href='./HojasEstilos/productos.css'>
                <title>Document</title>
            </head>
            <body>";

    echo "<div class='titulo'>TITULO: " . $nombreProductos . "</div>";
    
    echo "<div class='productos'>";
        array_walk($datos,function($element, $clave){
            echo "<div class='producto'>";
                array_walk($element,function($element, $clave){
                    //echo "$clave . $element <br> \n";
                    if($clave == "img"){
                        echo "<img src='$element'>";
                    }
                    if($clave == "nombre"){
                        echo "<a href='caca.html' class='titulo'>" . $element . "</a>";
                    }
                    if($clave == "descripcion"){
                        echo "<p class='descripcion'>" . $element . "</p>";
                    }
                    if($clave == "precio"){
                        echo "<h4 class='precio'>" . $element . "</h4>";
                    }
                });
            echo "</div>";
        });
    echo "</div>";
    echo "</body>
        </html>";   */
}



pintarProductos($nombreProductos, $DB);

print_r($_POST);

print_r(array_keys($_POST));

$arrayKey = array_keys($_POST);

$producto = $arrayKey[0];

echo $producto;

$numeroProducto = explode(",", $producto);

print_r("<br>quiere " . $_POST[$producto] . " " . $numeroProducto[1] . " de " . $numeroProducto[0]);


$DB->ejecuta(
    "INSERT INTO pedidio (nombre, cantidad, producto, nombreProducto, precio) VALUES (?,?,?,?,?)",
    "marcos",  $_POST[$producto], $numeroProducto[1], $numeroProducto[0], 
);
$insertado = $DB->getExecuted(); 
echo $insertado;
?>