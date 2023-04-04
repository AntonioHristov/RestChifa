<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../HojasEstilos/comun.css">
    <link rel="stylesheet" href="../HojasEstilos/menu.css">
    <link rel="stylesheet" href="../HojasEstilos/footer.css">
    <link rel="icon" href="../IMG/logo/shisha.png" type="image/gif" sizes="16x16">
    <script src="../javascript/menu.js" defer></script>
    <title>Menu</title>
</head>
<body>
    <div id="cabezera">
        <img src="../IMG/logo/shisha.png" alt="logo">
        <div id="nav">
            <ul>
                <li><a href="./index.php"><img src="../IMG/IconSVG/home-1-svgrepo-com.svg" alt="index"><span>INDEX</span></a></li>
                <li><a href="./menu.php"><img src="../IMG/IconSVG/menu-board-svgrepo-com.svg" alt="menu"><span>MENU</span></a></li>
                <li><a href="./reservas.php"><img src="../IMG/IconSVG/calendar-svgrepo-com.svg" alt="reservas"><span>RESERVAS</span></a></li>
                <li><a href="./nosotros.php"><img src="../IMG/IconSVG/users-svgrepo-com.svg" alt="nosotros"><span>NOSOTROS</span></a></li>
            </ul>
        </div>
    </div>
    <div id="Caja_Principal">
        <div id="titulo">
            <h1>MENU</h1>
        </div>
        <div id="listamenu">
            <img src="../IMG/IconSVG/menu-hamburger-nav-svgrepo-com.svg" alt="lista menu" id="listamenuIcon"/>
                <div class="list"><a href="http://localhost:8000/php/productos.php?nombreProductos=cocteles" target="ifram">COCTELES</a></div>
                <div class="list"><a href="http://localhost:8000/php/productos.php?nombreProductos=cachimbas" target="ifram">CACHIMBAS</a></div>
                <div class="list"><a href="http://localhost:8000/php/productos.php?nombreProductos=meriendas" target="ifram">MERIENDAS</a></div>
        </div>
        <div id="contenido">
            <iframe src="http://localhost:8000/php/productos.php?nombreProductos=cocteles" id="ifram" name="ifram" ></iframe>
        </div>
    </div>
    <div id="foote">
        <?php include_once('./footer.html') ?>
    </div>
</body>
</html>