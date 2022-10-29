#!/bin/bash
to="email"
echo " enter password"
read a
if [ $a != 1234 ]
then
	echo "try again"
	echo " enter password again"
	read b
	if [ $b != 1234 ] 
	then
		echo "alert bro "
		echo `fswebcam -r 640x480 --jpeg 85 -D 1 web-cam-shot.jpg` | sendmail -s "alert someone trying to access system" email
		echo `poweroff`

	else
		echo "welcome"
	fi
else
	echo "welcome"
fi
