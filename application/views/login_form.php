<!--Author: W3layouts
Author URL: http://w3layouts.com
License: Creative Commons Attribution 3.0 Unported
License URL: http://creativecommons.org/licenses/by/3.0/
-->
<!DOCTYPE HTML>
<html>
<head>
<title>Login DGD REMINDER</title>
<link href="<?php echo base_url('assets/css/styleLogin.css');?>" rel="stylesheet">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="keywords" content="Transparent Login Form Responsive Widget,Login form widgets, Sign up Web forms , Login signup Responsive web form,Flat Pricing table,Flat Drop downs,Registration Forms,News letter Forms,Elements" />
<!--web-fonts-->
<link href='//fonts.googleapis.com/css?family=Open+Sans:400,300,300italic,400italic,600,600italic,700,700italic,800,800italic' rel='stylesheet' type='text/css' />
<!--web-fonts-->
</head>

<body>
	<div class="header-w3l">
		<h1>Login</h1>
	</div>
    <?php echo form_open('user/login'); ?>
        <div class="main-content-agile">
            <div class="sub-main-w3">	
                <form action="#" method="post">
                    <!-- <input placeholder="Username or E-mail" name="Name" class="user" type="text" required=""><br> -->
                    <input placeholder="Username or E-mail" id="email" name="email" class="user" type="text"><br>
                    <input  placeholder="Password" name="password" class="pass" type="password" id="exampleInputPassword1"><br>
                    <input type="submit" value="">
                    <?php echo $this->session->flashdata('login_error'); ?>
                </form>
            </div>
        </div>
    <?php form_close(); ?>
<div class="footer">
	<p>&copy; 2019 DGD REMINDER. All rights reserved</p>
</div>
</body>
</html>
 
 
 
 
 <!-- <div class="container">

        <?php echo form_open('user/login'); ?>

        <div class="form-group">
            <label for="email">Email address</label>
            <input type="email" class="form-control" value="<?php echo set_value('email'); ?>" id="email" name="email" aria-describedby="emailHelp" placeholder="Enter email">
            <?php echo form_error('email'); ?>
        </div>
        <div class="form-group">
            <label for="password">Password</label>
            <input type="password" class="form-control" name="password" id="exampleInputPassword1" placeholder="Password">
            <?php echo form_error('password'); ?>
        </div>
        <button type="submit" class="btn btn-primary">Login</button>
        <?php echo $this->session->flashdata('login_error'); ?>
        
        <?php form_close(); ?>
    </div> -->