<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Index</title>
    <link rel="stylesheet" href="../HojasEstilos/index.css">
    <link rel="stylesheet" href="../HojasEstilos/comun.css">
    <link rel="stylesheet" href="../HojasEstilos/footer.css">
    <link rel="icon" href="../IMG/logo/shisha.png" type="image/png" sizes="16x16">
</head>
<body>
    <div id="cabezera">
        <img src="../IMG/logo/shisha.png" alt="logo">
        <div id="nav">
            <ul>
                <li><a href="./index.php"><img src="../IMG/IconSVG/home-1-svgrepo-com.svg" alt="index"><span>HOME</span></a></li>
                <li><a href="./menu.php"><img src="../IMG/IconSVG/menu-board-svgrepo-com.svg" alt="menu"><span>MENU</span></a></li>
                <li><a href="./reservas.php"><img src="../IMG/IconSVG/calendar-svgrepo-com.svg" alt="reservas"><span>RESERVAR</span></a></li>
                <li><a href="./nosotros.php"><img src="../IMG/IconSVG/users-svgrepo-com.svg" alt="nosotros"><span>NUESTRO</span></a></li>
            </ul>
        </div>
    </div>
    <div class="seccion1">
        <h1>Chanma</h1>
    </div>
    <div class="secciones">
        <h1>Tienda</h1>
        <img src="./../IMG/terraza.jpg" class="imgTienda">
        <p class="descripcion">
            Chanma lounge es una nueva teteria localizada en calle de la Caoba <br>justo al salir de la boca de metro de Acacias perfecta para pasar la tarde<br>
            con amigos en un sitio acogedor y accesible para  todos.<br> Ademas contamos con servicio de delivery para esas tardes improvisadas.
        </p>
    </div>

    <div class="secciones">
        <h1>Nuestro carta</h1>
        <img src="./../IMG/shisha.avif" class="imgCarta">
            <p class="descripcion"> 
                Entre nuestra carta podemos encontrar desde batidos o cocteles junto con <br> platos para compartir. Ademas podras disfrutar de nuestras<br>
                excelentes cachimbas con los sabores mas curiosos.
            </p>
        </div>
    </div>
    <div id="foote">
        <?php include_once('./footer.html') ?>
    </div>
</body>
</html>