<?php

$query_method = $_SERVER['REQUEST_METHOD'];

error_reporting(-1); // reports all errors
ini_set("display_errors", "1"); // shows all errors
ini_set("log_errors", 1);
ini_set("error_log", "php-error.log");

$sql_settings = 'mysql:host=localhost;port=8081;dbname=follow_plant_db;charset=utf8';
$db_username = "edison";
$db_pw = "followplant";

$db = new PDO($sql_settings,$db_username,$db_pw);

/*Grab post temperature variable*/
$temp = $_POST['temp'];

//grab existing data
$stmt = "Insert Into plant_temp (plant_temperature) Values (:plant_temperature)";
$query_stmt = $db->prepare($stmt);
$query_stmt->bindParam(':plant_temperature',$temp,PDO::PARAM_STR);
$query_stmt->execute();
$temp_id = $db->lastInsertId(); //can't use fetch all due to some server and db config

//if ($temp_id % 10 == 0){

	//send text message via Sinch - use curl to send
	$url = 'https://messagingApi.Sinch.com/v1/sms/+12482523866';
	$header = array('Content-Type: application/json; charset=utf-8');
	$fields_string = json_encode(array('message' => 'Your plant, Jimmy, is at '.$temp.' degrees Celsius.'));
	var_dump($fields_string);

	//set up curl connection
	$ch = curl_init($url); 
	curl_setopt($ch,CURLOPT_CUSTOMREQUEST,"POST");
	curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);
	//curl_setopt($ch,CURLOPT_URL,$url); //set url
	curl_setopt($ch,CURLOPT_HTTPAUTH, CURLAUTH_BASIC);
	curl_setopt($ch,CURLOPT_USERPWD,"application\\f7de985f-d24c-4911-be17-4dd116198f1a:ltx3SEX+uky/SMwmjj89Lw==");
	curl_setopt($ch,CURLOPT_HTTPHEADER,$header); //set header
	curl_setopt($ch,CURLOPT_POST,1); //set fields number
	curl_setopt($ch,CURLOPT_POSTFIELDS,$fields_string); //set other info
	curl_setopt($ch,CURLOPT_FOLLOWLOCATION,1);

	//execute post
	$result = curl_exec($ch);

	//close connection
	curl_close($ch);

	//every 100th temp, send email via sendgrid [calls python script]
	
//}
	
?>
