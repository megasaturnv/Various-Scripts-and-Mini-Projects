#!/bin/sh
#MegaSaturnv 2017-07-28
#Shell script / one-liner to parse and display an rss feed. May require tweaking for RSS feeds without newlines or where <title> and <description> are on separate lines to their text.

#Url of the RSS feed
RSS_URL=""

##Commented version:
#Download the rss feed
curl --silent "$RSS_URL" | \

#Only match lines with 'title>' or 'description>'
grep -E '(title>|description>)' | \

#Remove the first 3 lines
tail -n +4 | \
#Other methods which use sed instead of tail
  #sed -n '4,$p' | \
  #sed -e '1,3d' | \

#Remove all leading whitespace from each line (spaces and tabs)
sed -e 's/^[ \t]*//' | \

#Remove all title and description tags. '<description>' is replaced with '  ' to indent it
sed -e 's/<title>//' -e 's/<\/title>//' -e 's/<description>/  /' -e 's/<\/description>//'

###############################

##Command all on one line:
#curl --silent "$RSS_URL" | grep -E '(title>|description>)' | tail -n +4 | sed -e 's/^[ \t]*//' | sed -e 's/<title>//' -e 's/<\/title>//' -e 's/<description>/  /' -e 's/<\/description>//'
