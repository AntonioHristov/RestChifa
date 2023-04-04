<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../HojasEstilos/comunLoginRegistre.css">
    <link rel="stylesheet" href="../HojasEstilos/login.css">
    <link rel="stylesheet" href="../HojasEstilos/footer.css">
    <link rel="icon" href="../IMG/logo/shisha.png" type="image/gif" sizes="16x16">
    <script defer src="../javascript/comuLoginRegistre.js"></script>
    <title>Login</title>
</head>
<body>
    <div id="BoxForm">
        <form action="./index.php" method="post" id="LoginForm">
            <label id="imglogo"> <img src="../IMG/logo/shisha.png" alt="logo"></label>
            <label id="TitleForm">LOGIN/SING UP</label><br>
            <label>Telefono<br></label>
                <input type="text" value="+34 " id="SoloEspania" disabled>
                <input type="tel" maxlength="11" minlength="11" name="phone" id="phone" placeholder="xxx-xxx-xxx" required pattern="[0-9]{3}-[0-9]{3}-[0-9]{3}"><br>
                <img src="../IMG/IconSVG/eye-closed-svgrepo-com.svg" alt="ojo cerrado" id="eyeIcon">
            <label for="passw">Cotraseña<br> <input type="password" name="passw" id="passw" minlength="8" maxlength="16" placeholder="Introducer tu contraseña." required pattern="^(?=\w*\d)(?=\w*[A-Z])(?=\w*[a-z])\S{8,16}$"></label><br>
            <label><a href="./registre.php" id="Rlink">Registre</a></label><br>
            <label for="Login"><input type="submit" value="Login" name="Login" id="Login"></label>
        </form>
    </div>
    <div id="foote">
        <?php include_once('./footer.html') ?>
    </div>
</body>
</html>