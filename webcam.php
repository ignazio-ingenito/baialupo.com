<?php
$url = "http://95.243.125.62:8089/cgi-bin/image.cgi?userName=webcam&password=Webc@m12654&cameraID=1&quality=9";
$img = "/web/htdocs/www.baialupo.com/home/web/images/webcam.new.jpg";

$cmd = "wget -q \"$url\" -O \"$img\" >> log.log 2>&1 & ";
$out = exec($cmd);

while ( filesize($img) <= 0 ) {
	sleep(5);
}

try {
	rename("webcam.jpg","webcam.old.jpg");
	rename("webcam.new.jpg","webcam.jpg");
	unlink("webcam.old.jpg");
	unlink("log.log");
}
catch (Exception $e) {
}
?>

<html lang="it">
<head>
</head>
<body>
	<?=$out?><br /><br />
	<img id='webcam' src="images/webcam.jpg" border='0' />
</body>
</html>