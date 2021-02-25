#!/bin/sh
#MegaSaturnv 2017-07-28
#Shell one-liner to echo / print the number of days until christmas (or any other arbitrary date)
echo $(($(date -d 25-Dec +%-j) - $(date +%-j))) days until christmas!