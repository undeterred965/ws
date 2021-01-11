<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Reboot</title>
</head>

<body>

<p>Restarting server...</p>
<?php
echo exec('/home/pi/scripts/server_restart.sh');
?>

</body>
</html>

