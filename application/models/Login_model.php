<?php
class Login_model extends CI_Model{

  function validate($email,$password){
    $this->db->where('mail',$email);
    $this->db->where('password',$password);
    $result = $this->db->get('user',1);
    return $result;
  }

}
