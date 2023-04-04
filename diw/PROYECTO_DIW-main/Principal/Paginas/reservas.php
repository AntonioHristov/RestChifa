<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reservas</title>
    <link rel="stylesheet" href="../HojasEstilos/reservas.css">
    <link rel="stylesheet" href="../HojasEstilos/footer.css">
    <link rel="stylesheet" href="../HojasEstilos/comun.css">
    <link rel="icon" href="../IMG/logo/shisha.png" type="image/gif" sizes="16x16">
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
    <div id="div_general">
        <div id="div_titulo_reservas">
            <h2>RESERVAS</h2>
        </div>
        <form action="./menu.html" method="post" id="formulario">
            <fieldset class="fieldsetcomun" id="seleeccion_mesa">
                <legend> SELECCIÓN MESA </legend>
                <p class="posicion1">A-1</p>
                <p class="posicion2">A-2</p>
                <p class="posicion3">A-3</p>
                <p class="posicion4">A-4</p>
                <label><input type="checkbox" class="checkbox_reservas" name="checkbox_reservas"/></label>
                <label><input type="checkbox" class="checkbox_reservas" name="checkbox_reservas"/></label>
                <label><input type="checkbox" class="checkbox_reservas" name="checkbox_reservas"/></label>
                <label><input type="checkbox" class="checkbox_reservas" name="checkbox_reservas"/></label>
                <br>

                <p class="posicion1">B-1</p>
                <p class="posicion2">B-2</p>
                <p class="posicion3">B-3</p>
                <p class="posicion4">B-4</p>
                <label><input type="checkbox" class="checkbox_reservas" name="checkbox_reservas"/></label>
                <label><input type="checkbox" class="checkbox_reservas" name="checkbox_reservas"/></label>
                <label><input type="checkbox" class="checkbox_reservas" name="checkbox_reservas"/></label>
                <label><input type="checkbox" class="checkbox_reservas" name="checkbox_reservas"/></label>
                <br>

                <p class="posicion1">C-1</p>
                <p class="posicion2">C-2</p>
                <p class="posicion3">C-3</p>
                <p class="posicion4">C-4</p>
                <label><input type="checkbox" class="checkbox_reservas" name="checkbox_reservas"/></label>
                <label><input type="checkbox" class="checkbox_reservas" name="checkbox_reservas"/></label>
                <label><input type="checkbox" class="checkbox_reservas" name="checkbox_reservas"/></label>
                <label><input type="checkbox" class="checkbox_reservas" name="checkbox_reservas"/></label>
                <br>

                <p class="posicion1">D-1</p>
                <p class="posicion2">D-2</p>
                <p class="posicion3">D-3</p>
                <p class="posicion4">D-4</p>
                <label><input type="checkbox" class="checkbox_reservas" name="checkbox_reservas"/></label>
                <label><input type="checkbox" class="checkbox_reservas" name="checkbox_reservas"/></label>
                <label><input type="checkbox" class="checkbox_reservas" name="checkbox_reservas"/></label>
                <label><input type="checkbox" class="checkbox_reservas" name="checkbox_reservas"/></label> 
            </fieldset>
            <span id="saltoLinea"></span>
            <fieldset class="fieldsetcomun" id="seleeccion_comun">
                <legend>SELECCIÓN GENERAL</legend>
                <fieldset id="fecha">
                    <legend>FECHA</legend>
                    <label><input type="date" name="fecha" required/></label>
                </fieldset>
                <fieldset id="hora">
                    <legend>HORA</legend>
                    <label><input type="time" name="hora" required/></label>
                </fieldset>
                <fieldset id="persona">
                    <legend>PERSONAS</legend>
                    <label><input type="number" name="persona" max="15" min="1" size="5" required/></label>
                </fieldset>
                <label for="boton_enviar"><input id="boton_enviar" type="submit" value="ENVIAR"/></label>
            </fieldset>
        </form>
    </div>
    <div id="foote">
        <?php include_once('./footer.html') ?>
    </div>
</body>
</html>