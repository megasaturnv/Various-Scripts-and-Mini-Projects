# OctoPrintTimelapseTimeStamp.py
Allows a custom timestamp and text to be added to Octoprint's timelapses. 

### Requirements
* PIL / Pillow - Image manipulation for python. Install with one of the following. Run as root (sudo ...)
  * apt install python3-pillow python3-pil
  * yum install python3-pillow python3-pil
  * pacman -S python3-pillow python3-pil
  * pip3 install PIL
  * pip3 install pillow
* Fonts
  * apt install fontconfig fonts-dejavu-core


### Installation
* Save OctoPrintTimelapseTimeStamp.py to ~/OctoPrint/scripts/
* Backup config.yaml `cp ~/.octoprint/config.yaml ~/.octoprint/BACKUPconfig.yaml`
* Edit ~/.octoprint/config.yaml `nano ~/.octoprint/config.yaml`
* Add the following:
```
events:
    subscriptions:
    -   command: python3 ~/OctoPrint/scripts/timestamp_timelapse.py "{file}"
        event: CaptureDone
        type: system
```

### Alternative command for logging:
```
command: python3 ~/OctoPrint/scripts/timestamp_timelapse.py "{file}" &>> ~/OctoPrint/scripts/timestamp_timelapse.log
```

### Additional
* You may wish to change the hashbang to "#!/home/<user>/OctoPrint/venv/bin/python" to use octoprint's python, though you're on your own with pip. This code should run under python2 and python3
* Based off the code submitted here: https://community.octoprint.org/t/solution-date-time-on-timelapse/5571/6
* Octoprint events documentation: https://docs.octoprint.org/en/master/events/index.html

### Todo:
* Add example image to readme
* Add more options for text position (e.g. top-left, top-right, bottom-left, bottom-right)