<?php

$serverName = "SQL Server"; 
$uid = "CoachLogin";   
$pwd = "toast&s3ri@l#s";  
$databaseName = "LoperSlamdUNK"; 

$connectionInfo = array( "UID"=>$uid,                            
                         "PWD"=>$pwd,                            
                         "Database"=>$databaseName); 

/* Connect using SQL Server Authentication. */  
$con = odbc_connect("Driver=$serverName; Server=localhost; Database=$databaseName", $uid, $pwd);

if(!$con){
  echo "Database not connected";
}
else{
}

 ?>
