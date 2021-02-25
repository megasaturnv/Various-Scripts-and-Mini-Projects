<?php
//MegaSaturnv 2018-01-16
//Display snapshot from usb webcam camera /dev/video0 on a webpage. No temp file. Uses avconv command
header("content-type: image/jpeg");
//                        Change this resolution to match your camera \/
echo passthru("avconv -f video4linux2 -i /dev/video0 -vframes 1 -s 1920x1080 pipe:.jpg 2>/dev/null");
?>
