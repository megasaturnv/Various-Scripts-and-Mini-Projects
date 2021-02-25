<?php /*MegaSaturnv 2018-01-16
Download and display image from remote webpage. No temp file. Image in <img> tag

Use curl -u username:password for http auth if required*/ ?>
<img src="data:image/jpeg;base64, <?php echo base64_encode(shell_exec("curl http://192.168.1.50/cgi-bin/snapshot.cgi?channel=0 2> /dev/null")) ?>">