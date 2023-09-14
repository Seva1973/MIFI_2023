<html lang="en">
<head>
<title>Russian Far East Regions</title>
    <link rel="stylesheet" href="style.css" type="text/css"/>
</head>
<body>
<h1>Regions</h1>
<table>
    <tr><th>region</th><th>maincity</th><th>population</th></tr>
<?php
$mysqli = new mysqli("database", "user", "password", "reg1");
$result = $mysqli->query("SELECT * FROM regions");
foreach ($result as $row){
    echo "<tr><td>{$row['region']}</td><td>{$row['maincity']}</td><td>{$row['population']}</td></tr>";
}
?>
</table>
<?php
phpinfo();
?>
</body>
</html>

