<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class User extends CI_Controller {

	public function __construct() {
		parent::__construct();
		$this->load->helper(array('form', 'url'));
		$this->load->library(['form_validation','session']);
		$this->load->database();
	}

	public function login() {
        // session_start();
		$this->form_validation->set_rules('email', 'Email', 'required');
		$this->form_validation->set_rules('password', 'Password', 'required');

		if ($this->form_validation->run() == FALSE) {
			$this->load->view('login_form');
		} else {

			$email = $this->input->post('email');
			$password = $this->input->post('password');

			$user = $this->db->get_where('users',['email' => $email])->row();
			
			if(!$user) {
				$this->session->set_flashdata('login_error', 'Please check your email or password and try again.', 300);
				redirect(uri_string());
			}

	
			if(!password_verify($password,$user->password)) {
				$this->session->set_flashdata('login_error', 'Please check your email or password and try again.', 300);
				redirect(uri_string());
			}

			 $data = array(
					'user_id' => $user->user_id,
					'first_name' => $user->first_name,
					'last_name' => $user->last_name,
					'email' => $user->email,
					);

            $_SESSION['user_id'] = $user->user_id;
			$this->session->set_userdata($data);

            //redirect('/'); // redirect to home
            redirect('Inicio');
			// echo 'Login success!'; exit;
			
		}		
	}

	public function logout(){
        $this->session->sess_destroy();
        redirect('user/login');
    }

}