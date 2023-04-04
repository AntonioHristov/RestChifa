<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../HojasEstilos/comun.css">
    <link rel="stylesheet" href="../HojasEstilos/comunicanos.css">
    <link rel="stylesheet" href="../HojasEstilos/footer.css">
    <link rel="icon" href="../IMG/logo/shisha.png" type="image/gif" sizes="16x16">
    <title>Asundo</title>
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
    <div>
        <h1 id="titulo">Comunicar con Nosotros</h1>
        <form action="./index.php" method="post">
            <label for="username">Nombre <input type="text" name="username" id="username" placeholder="Nombre y Apellido" required></label><br>
            <label for="correo" id="labelCorreo">Correo <input type="email" name="correo" placeholder="Correo Electronico" id="correo" required></label><br>
            <p>Mensaje: </p><textarea name="asundo" id="asundo">Mensaje</textarea><br>
            <p id="parrafoUpFile">¿Deseas Ajuntar algun archivo?</p>
            <label for="upfile"><input type="file" name="upfile" id="upfile"></label><br>
            <label for="Enviar"><input type="submit" value="Enviar" id="enviar"></label>
        </form>
    </div>
    <div id="foote">
        <?php include_once('./footer.html') ?>
    </div>
</body>
</html>