<?php
$requiredEnvVars = ['DB_HOST', 'DB_PORT', 'DB_USERNAME', 'DB_PASSWORD'];

foreach ($requiredEnvVars as $envVar) {
    if (!isset($_SERVER[$envVar]) || empty($_SERVER[$envVar])) {
        echo "Переменная окружения $envVar не установлена или не содержит значения.";
        // Можно выполнить дополнительные действия, если необходимо
        exit;
    }
}
// Все переменные окружения установлены
$host = $_SERVER['DB_HOST'];
$port = $_SERVER['DB_PORT'];
$database = 'world';
$username = base64_decode(getenv('DB_USERNAME'));
$password = base64_decode(getenv('DB_PASSWORD'));

// Продолжайте выполнение кода подключения к базе данных и выполнения запроса
// ...

// Подключение к базе данных MySQL
$host = $_SERVER['DB_HOST'];
$port = $_SERVER['DB_PORT'];
$database = 'world';
$username = base64_decode(getenv('DB_USERNAME'));
$password = base64_decode(getenv('DB_PASSWORD'));

$dsn = "mysql:host=$host;port=$port;dbname=$database;charset=utf8mb4";
try {
    $pdo = new PDO($dsn, $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Выполнение запроса к таблице
    $stmt = $pdo->query("SELECT * FROM city"); // city - имя таблицы.
    $rows = $stmt->fetchAll(PDO::FETCH_ASSOC);

    // Вывод результатов
    foreach ($rows as $row) {
        echo "ID: " . $row['ID'] . ", Name: " . $row['Name'] . ", CountryCode: " . $row['CountryCode'] . 
        ", District: " . $row['District'] . ", Population: " . $row['Population'] ."<br>";
    }
} catch (PDOException $e) {
    echo "Ошибка подключения к базе данных: " . $e->getMessage();
}
?>
