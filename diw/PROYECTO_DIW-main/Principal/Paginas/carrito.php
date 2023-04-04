<?php

require("./../php/src/init.php");

echo "<a href='http://localhost:8000/php/productosComprar.php?nombreProductos=cocteles'>menu</a><br>";

/*function buscarIguales($array){
    $valores = array_count_values($array);
    return $valores;
}

function mostarPedido($array){
    $pedido = $array[0]['nombreProducto'];
    $arraypedido = explode(',', $pedido);
    return buscarIguales(($arraypedido));
}

function formato($array){

    echo "<table>
            <tr><td>Producto</td><td>Cantidad</td></tr>";
            array_walk($array, function($value, $key){
                echo "<tr><td>$key</td><td>X$value</td></tr>";
            });
        echo "</table>";
}

function precioTotal($array, $DB){
    $pedido = $array[0]['nombreProducto'];
    $arraypedido = explode(',', $pedido);
    $arrayPrecioTotal = [];

    $DB->ejecuta("SELECT precio,nombre FROM productos");
    $datos = $DB->obtenDatos();

    $precios = $datos;

    $DB->ejecuta("SELECT nombre FROM productos");
    $datos = $DB->obtenDatos();

    $nombres = $datos;

    for($i = 0; $i < count($precios); $i++){
        $arrayPrecios[$nombres[$i]['nombre']] = $precios[$i]['precio'];
    }

    $contadorPrecio = 0;
    for($i = 0; $i < count($arraypedido); $i++){
        $contadorPrecio += $arrayPrecios[$arraypedido[$i]];
    }

    return $contadorPrecio;
}

if(isset($_COOKIE['producto'])){

    $DB->ejecuta("SELECT * FROM pedido WHERE nombre = ?", $_SESSION['nombre']);
    $datos = $DB->obtenDatos();

    if(empty($datos)){
        $DB->ejecuta(
            "INSERT INTO pedido (nombre, nombreProducto) VALUES (?,?)",
            $_SESSION['nombre'],  $_COOKIE['producto']
        );
        $insertado = $DB->getExecuted(); 
        if($insertado){
            $DB->ejecuta("SELECT * FROM pedido WHERE nombre = ?", $_SESSION['nombre']);
            $datos = $DB->obtenDatos();
            echo "nuevo pedido registrado<br>";
            $DB->ejecuta("SELECT * FROM pedido WHERE nombre = ?", $_SESSION['nombre']);
            $datos = $DB->obtenDatos();

            $pedido = mostarPedido($datos);
            formato($pedido);
            print_r(precioTotal($datos, $DB));
            setcookie('producto','',time() - 1,'/'); 


            echo "<form method='post'><input type='submit' value='pagar' name='pagar'></form>";
        }
    }else{
        $pedido = $datos[0]['nombreProducto'] . "," . $_COOKIE['producto'];
        $pedido;

        $DB->ejecuta(
            "UPDATE pedido SET nombreProducto = ? WHERE nombre = ?",
            $pedido, $_SESSION['nombre']
        );    

        $cambiado = $DB->getExecuted();
        if($cambiado){
            $DB->ejecuta("SELECT * FROM pedido WHERE nombre = ?", $_SESSION['nombre']);
            $datos = $DB->obtenDatos();

            
            echo "nuevo producto añadido<br>";
            $DB->ejecuta("SELECT * FROM pedido WHERE nombre = ?", $_SESSION['nombre']);
            $datos = $DB->obtenDatos();

            $pedido = mostarPedido($datos);
            formato($pedido);
            print_r(precioTotal($datos, $DB));
            setcookie('producto','',time() - 1,'/');

            echo "<form method='post'><input type='submit' value='pagar' name='pagar'></form>";
        }
    }
}else{
    $DB->ejecuta("SELECT * FROM pedido WHERE nombre = ?", $_SESSION['nombre']);
    $datos = $DB->obtenDatos();
    if(empty($datos)){
        echo "COMIENZA UN NUEVO PEDIDO <a href='menu.html'>COMPRAR</a>";
    }else{
        $pedido = mostarPedido($datos);
        formato($pedido);
        print_r(precioTotal($datos, $DB));
        echo "<form method='post'><input type='submit' value='pagar' name='pagar'></form>";
    }
}

/*if(isset($_POST['pagar'])){
    $DB->ejecuta(
        "DELETE FROM pedido WHERE nombre = ?",
        $_SESSION['nombre']
    );

    $borrado = $DB->getExecuted();

    if($borrado){
        header("Location: ./../Paginas/pagoTarjeta.html");
        die();
    }
}*/



    $DB->ejecuta(
        "INSERT INTO pedido (nombre, nombreProducto) VALUES (?,?)",
        $_SESSION['nombre'],  $_POST['nombre']
    );
    $insertado = $DB->getExecuted(); 
    if($insertado){

        echo "insertado";
    }

?>