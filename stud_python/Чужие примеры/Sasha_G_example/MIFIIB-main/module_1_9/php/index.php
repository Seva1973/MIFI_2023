<html lang="en">

<head>
    <title>Our Instruments</title>
    <link rel="stylesheet" href="style.css" type="text/css" />
</head>

<body>
    <h1>Instruments</h1>
    <table style="border:1px solid black;margin-left:auto;margin-right:auto;">
        <tr>
            <th>ID</th>
            <th>BRAND</th>
            <th>MODEL</th>
        </tr>
        <?php
        $mysqli = new mysqli("db", "user", "password", "instruments");
        $result = $mysqli->query("SELECT * FROM guitars");
        foreach ($result as $row) {
            echo "<tr><td>{$row['id']}</td><td>{$row['brand']}</td><td>{$row['model']}</td></tr>";
        }
        ?>
    </table>
    <?php
    phpinfo();
    ?>
</body>

</html>