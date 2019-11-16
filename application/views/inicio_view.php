<?php
// You'd put this code at the top of any "protected" page you create

// Always start this first
// session_start();

if ( isset( $_SESSION['user_id'] ) ) {
    // Grab user data from the database using the user_id
    // Let them access the "logged in only" pages
} else {
    // Redirect them to the login page
    // header("Location: http://www.yourdomain.com/login.php");
    redirect('user/login');
}
?>
<!-- <!DOCTYPE html>
<html lang="en">
  <head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    
    <title>DGD REMINDER</title>
    <link href="<?php echo base_url('assets/css/bootstrap.min.css');?>" rel="stylesheet">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  </head>
  <body>
  <h1>Hola</h1>

  </body>
</html> -->

<html>
  <head>
    <title>DGD REMINDER</title>
    
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <link href="https://fonts.googleapis.com/css?family=Poppins" rel="stylesheet" />
    <link href="<?php echo base_url('assets/css/inicio.css');?>" rel="stylesheet" />
  </head>
  <body>
    <div class="s01">
    <form action="<?php echo base_url()?>Inicio/inicioGuarda" method="POST">
        <fieldset>
          <legend>DGD REMINDER</legend>
        </fieldset>
        <form action="<?php echo base_url()?>index.php/Welcome/toView2" method="POST">
          <div class="inner-form">
            <div class="input-field first-wrap">
              <input id="mensaje" name="mensaje" type="text" placeholder="Mensaje" required pattern="[A-Za-z0-9 ñ]+ ?"/>
            </div>
            <div class="input-field second-wrap">
              <input id="fecha" name="fecha" type="datetime-local" placeholder="Fecha" required/>
            </div>
            <div class="input-field third-wrap">
              <button class="btn-search" type="submit">Guardar</button>
            </div>
          </div>
          </form>
    </div>
  </body>
</html>






