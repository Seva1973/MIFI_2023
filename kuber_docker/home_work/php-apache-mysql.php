<?php
$host = '10.98.45.84'; 
$port = '3306';
$username = 'root';
$password = 'qw9999zx';
$database = 'world';

$conn = new mysqli($host, $username, $password, $database);

if ($conn->connect_error) {
    die('Ошибка подключения к базе данных: ' . $conn->connect_error);
}

$query = 'SELECT * FROM city'; 

$result = $conn->query($query);

if ($result->num_rows > 0) {
    echo '<table>';
    echo '<tr><th>ID</th><th>Name</th><th>CountryCode</th><th>District</th><th>Population</th></tr>';

    while ($row = $result->fetch_assoc()) {
        echo '<tr>';
        echo '<td>' . $row['ID'] . '</td>';
        echo '<td>' . $row['Name'] . '</td>';
        echo '<td>' . $row['CountryCode'] . '</td>';
        echo '<td>' . $row['District'] . '</td>';
        echo '<td>' . $row['Population'] . '</td>';
        echo '</tr>';
    }

    echo '</table>';
} else {
    echo 'Нет данных для отображения.';
}
