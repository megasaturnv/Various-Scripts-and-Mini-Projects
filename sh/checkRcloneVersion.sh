#!/bin/sh
#MegaSaturnv 2018-01-08
#Check Rclone version. Checks version from https://rclone.org/downloads/ and compares it to current version in checkRcloneVersion_current.txt, which needs to be updated after a new version of rclone is installed

# Uncomment to create checkRcloneVersion_current.txt file:
# echo v1.38 > checkRcloneVersion_current.txt

# Add following line to crontab (crontab -e) to check once a week (every Monday at 21:21)
# 21 21 * * 1 ./checkRcloneVersion.sh

LOCAL_VERSION="$(cat checkRcloneVersion_current.txt)"
SERVER_VERSION="$(curl --silent 'https://rclone.org/downloads/' | grep -P 'Rclone Download v\d*\.\d*' | grep -Po 'v\d*\.\d*')"

if [ "$LOCAL_VERSION" != "$SERVER_VERSION" ]; then
    # Add message to the end of current user's .bashrc file
    echo "echo There is an update for rclone. Current version is: $LOCAL_VERSION. New version is: $SERVER_VERSION" >> "$HOME/.bashrc"
    # Optional. Add message to /etc/motd/
    #echo "There is an update for rclone. Current version is: $LOCAL_VERSION. New version is: $SERVER_VERSION" >> '/etc/motd'
fi