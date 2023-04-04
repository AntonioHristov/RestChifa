<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../HojasEstilos/nosotros.css">
    <link rel="stylesheet" href="../HojasEstilos/comun.css">
    <link rel="stylesheet" href="../HojasEstilos/footer.css">
    <link rel="icon" href="../IMG/logo/shisha.png" type="image/gif" sizes="16x16">
    <script src="../javascript/nosotros.js" defer></script>
    <title>Nosotros</title>
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
    <div id="cajaPrincipa">
        <div id="titulo">
            <h1>NOSOTROS</h1>
        </div>
        <div id="bannermedia">
            <div id="imagenes">
                <img src="../IMG/carbon.png" alt="">
                <img src="../IMG/peter-day-YsM3ZfFh-tM-unsplash.jpg" alt="">
                <img src="../IMG/shisha.avif" alt="">
                <img src="../IMG/awesome-sauce-creative-_ynhWwRBKXk-unsplash.jpg" alt="">
                <img src="../IMG/terraza.jpg" alt="">
            </div>
            <div id="dots">
                <span class="dot active" data-index="0"></span>
                <span class="dot" data-index="1"></span>
                <span class="dot" data-index="2"></span>
                <span class="dot" data-index="3"></span>
                <span class="dot" data-index="4"></span>
            </div>
        </div>
        <div id="video" class="videoaudio">
            <h1>Nuestro BAR</h1>
            <video src="../videoAudio/playa-959.mp4" autoplay muted controls></video>
        </div>
        <div id="audio" class="videoaudio">
            <h1>Nuestro Audio</h1>
            <audio src="../videoAudio/010790638_prev.mp3" autoplay controls></audio>
        </div>
    </div>
    <div id="foote">
        <?php include_once('./footer.html') ?>
    </div>
</body>
</html>