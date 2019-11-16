<?php
class Login extends CI_Controller{
  function __construct(){
    parent::__construct();
    $this->load->model('login_model');
  }

  function index(){
    $this->load->view('inicio_view');
  }

  function auth(){
    $email    = $this->input->post('username',TRUE);//email
    $password = $this->input->post('password',TRUE);
    // $id_comp = $this->input->post('id_comp',TRUE);
    $validate = $this->login_model->validate($email,$password,$id_comp);
    if($validate->num_rows() > 0){
        $data  = $validate->row_array();
        $name  = $data['user_name'];
        $email = $data['user_email'];
        $level = $data['user_level'];
        $nombreCompleto=$data['nombre_completo'];
        $sesdata = array(
            'username'  => $name,
            'email'     => $email,
            'level'     => $level,
            'logged_in' => TRUE,
            'centroCosto' => $centroCosto,
            // 'id_comp'=>$id_comp,
            'nombre_completo'=>$nombreCompleto
        );
        $this->session->set_userdata($sesdata);
        // access login for admin
        if($level === 'admin'){
            redirect('administracion');

        // access login for staff
        }elseif($level === 'cliente'){
            redirect('cliente');

        // access login for author
        }else{
            redirect('administracion/author');
        }
    }else{
        echo $this->session->set_flashdata('msg','Usuario o Contraseña incorrectos');
        redirect('login');
    }
  }

  function logout(){
      $this->session->sess_destroy();
      redirect('login');
  }

}
