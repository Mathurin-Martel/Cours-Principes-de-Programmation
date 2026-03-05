<?php
require_once 'config/config.php';
class StudentService{
    public static function getAllStudents(){
        $url = API_BASE_URL . 'students';
        $reponse=file_get_contents($url);
        return $students=json_decode($reponse,true);
    }
}
