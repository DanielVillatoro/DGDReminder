<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Inicio extends CI_Controller {
	public function __construct() {
		parent::__construct();
		$this->load->helper(array('form', 'url'));
		$this->load->library(['form_validation','session']);
		$this->load->database();
	}

	public function index()
	{
		$this->load->view('inicio_view');
	}

	public function inicioGuarda(){
		$mensaje = $this->input->post('mensaje');
		$fecha = $this->input->post('fecha');
		$this->load->view('inicio_view');
		$this->db->query("INSERT INTO recordatorio VALUES('0','$mensaje','$fecha','1')");
		// echo $mensaje;
		// echo $fecha;
	}
}
