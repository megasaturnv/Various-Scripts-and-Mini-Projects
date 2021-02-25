#!/bin/sh
#MegaSaturnv 2017-06-08
#One-liner to check newsbeuter for updates every 30 seconds. If an unread item apears, it will alert the user with an audible bell and open newsbeuter. https://github.com/akrennmair/newsbeuter http://www.newsbeuter.org/

#May also work with newsboat by doing a simple replace below. newsbeuter -> newsboat
while true; do sleep 30; newsbeuter -x reload -x print-unread | grep -q "^0 unread articles" && echo -n . || (echo -e "\a"; newsbeuter) ; done