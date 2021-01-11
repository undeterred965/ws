<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Shutdown</title>
</head>

<body>

<p>Shutting down server...</p>
<?php
echo exec('/home/pi/scripts/server_shutdown.sh');
?>

</body>
</html>

