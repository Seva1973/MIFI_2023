<?php
$host = '10.98.45.84'; 
$port = '3306';
$username = 'root';
$password = 'qw9999zx';
$database = 'world';

$dsn = "mysql:host=$host;port=$port;dbname=$database;charset=utf8mb4";

try {
    $pdo = new PDO($dsn, $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    $query = 'SELECT * FROM city'; 
    $statement = $pdo->query($query);

    if ($statement->rowCount() > 0) {
        echo '<table>';
        echo '<tr><th>ID</th><th>Name</th><th>CountryCode</th><th>District</th><th>Population</th></tr>';

        while ($row = $statement->fetch(PDO::FETCH_ASSOC)) {
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
} catch (PDOException $e) {
    die('Ошибка подключения к базе данных: ' . $e->getMessage());
}
?>
