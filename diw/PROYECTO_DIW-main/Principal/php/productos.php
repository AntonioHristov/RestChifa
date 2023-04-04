<?php

require("src/init.php");

if(isset($_GET['nombreProductos'])){
    $nombreProductos = $_GET['nombreProductos'];
}

function pintarProductos($nombreProductos, $DB){
    
    $cookie = "producto";

    $DB->ejecuta("SELECT * FROM productos where categoria = ?", $nombreProductos);
    $datos = $DB->obtenDatos();

    echo "<!DOCTYPE html>
            <html lang='en'>
            <head>
                <meta charset='UTF-8'>
                <meta http-equiv='X-UA-Compatible' content='IE=edge'>
                <meta name='viewport' content='width=device-width, initial-scale=1.0'>
                <link rel='stylesheet' href='./../HojasEstilos/productos.css'>
                <title>Document</title>
                <script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js'></script>
                <script src='contador.js' defer></script>
            </head>
            <body>";

    echo "<div class='titulo'>" . strtoupper($nombreProductos) . "</div>";
    
    echo "<div class='productos'>";
        array_walk($datos,function($element, $clave){
            echo "<div class='producto'>";

                echo "<div class='info'>";
                
                    echo "<div class='contieneNombre'>";
                        echo "<a class='nombre'>" . $element['nombre'] . "</a>";
                    echo "</div>";

                    
                        echo "<img src='" . $element['img'] . "' class='image'>";
                    

                    echo "<div class='contieneDescripcionPrecioFoto'>";

                        echo "<div class='contieneDescripcionPrecio'>";
                            echo "<p class='descripcion'>" . $element['descripcion'] . "</p>";
                            echo "<h4 class='precio'>" . $element['precio'] . "€</h4>";
                        echo "</div>";
                    echo "</div>";

                echo "</div>";
            echo "</div>";
        });
    echo "</div>
        </body>
        </html>";
}

pintarProductos($nombreProductos, $DB);


?>