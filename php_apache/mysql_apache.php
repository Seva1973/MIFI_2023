<?php
// Параметры подключения к базе данных MySQL
$host = 'localhost'; // Хост (обычно localhost)
$username = 'root'; // Имя пользователя MySQL
$password = '1596321'; // Пароль пользователя MySQL
$database = 'world'; // Имя базы данных MySQL

// Установка соединения с базой данных
$conn = new mysqli($host, $username, $password, $database);

// Проверка соединения на наличие ошибок
if ($conn->connect_error) {
    die('Ошибка подключения к базе данных: ' . $conn->connect_error);
}

// Выполнение SQL-запроса для получения данных из таблицы в базе данных
$query = 'SELECT * FROM city'; // Замените "table_name" на имя вашей таблицы

$result = $conn->query($query);

// Проверка наличия данных
if ($result->num_rows > 0) {
    // Вывод данных в виде таблицы
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

// Закрытие соединения с базой данных
$conn->close();
?>
