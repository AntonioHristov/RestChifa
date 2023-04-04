<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registre</title>
    <link rel="stylesheet" href="../HojasEstilos/registre.css">
    <link rel="stylesheet" href="../HojasEstilos/comunLoginRegistre.css">
    <link rel="stylesheet" href="../HojasEstilos/footer.css">
    <link rel="icon" href="../IMG/logo/shisha.png" type="image/gif" sizes="16x16">
    <script src="../javascript/registre.js" defer></script>
    <script src="../javascript/comuLoginRegistre.js" defer></script>
</head>
<body>
    <div id="BoxForm">
        <form action="./login.php" method="post" id="RegistForm">
            <label id="imglogo"> <img src="../IMG/logo/shisha.png" alt="logo"></label>
            <label id="TitleForm">REGISTRE</label><br>
            <label>Telefono</label><br>
                <input type="text" value="+34 " id="SoloEspania" disabled>
                <input type="tel" maxlength="11" minlength="11" name="phone" id="phone" placeholder="xxx-xxx-xxx" required pattern="[0-9]{3}-[0-9]{3}-[0-9]{3}"><br>
                <img src="../IMG/IconSVG/eye-closed-svgrepo-com.svg" alt="ojo cerrado" id="eyeIconR1">
            <label for="regist_passw">Contraseña<br> <input type="password" name="Rpasswd1" id="Rpasswd1" minlength="8" maxlength="16" placeholder="Introducer contraseña." required pattern="^(?=\w*\d)(?=\w*[A-Z])(?=\w*[a-z])\S{8,16}$"></label><br>
                <img src="../IMG/IconSVG/eye-closed-svgrepo-com.svg" alt="ojo cerrado" id="eyeIconR2">
            <label for="repit_regist_passw">Repite Contraseña<br> <input type="password" name="Rpasswd2" id="Rpasswd2" minlength="8" maxlength="16" placeholder="Repite contraseña de nuevo." required pattern="^(?=\w*\d)(?=\w*[A-Z])(?=\w*[a-z])\S{8,16}$"><span id="erro"></span></label><br>
            <label for="Registre"><input type="submit" value="Registre" name="Registre" id="Registre"></label>
        </form>
    </div>
    <div id="foote">
        <?php include_once('./footer.html') ?>
    </div>
</body>
</html>