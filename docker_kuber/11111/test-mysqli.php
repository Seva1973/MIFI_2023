<?php
$host = '10.98.45.84'; 
$port = '3306';
$username = 'Seva1973';
$password = 'qw9999zx';

$connection = new mysqli($host, $username, $password, '', $port);
if ($connection->connect_error) {
    die('Ошибка подключения к базе данных: ' . $connection->connect_error);
}

$result = $connection->query('SELECT VERSION()');
$row = $result->fetch_assoc();
echo 'Версия MySQL: ' . $row['VERSION()'];

$connection->close();
?>