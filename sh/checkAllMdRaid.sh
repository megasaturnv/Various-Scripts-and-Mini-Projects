#!/bin/bash

# MegaSaturnv 2021-03-20

# A script to check all MD RAID devices aka Linux Software RAID. Will print one line of text for each degraded RAID.
# Designed to be placed in .bashrc to notify the user of any issues.
# You can also run "./checkAllMdRaid.sh -v" to show the state of all RAID devices, rather than just the degraded ones.

# Unfortunately, this has to be run as root. A version is WIP that only reads /proc/mdstat so a non-root user can run this

# Add the following line to .bashrc, filling in the actual file path:
# /path/to/file/checkAllMdRaid.sh

# The line "MAILADDR root" in /etc/mdadm.conf will also notify the user, if setup correctly

############
# Settings #
############
regexQuery="^\s*?State : (clean|active)\s*?$"

##########
# Checks #
##########
if [[ $EUID -ne 0 ]]; then
	echo "mdadm requires this script be run as root"
	exit 1
fi
if [ ! -f /proc/mdstat ]; then
	echo "/proc/mdstat does not exist. Likely there are no MD RAIDs or mdadm is not installed"
	exit 1
fi

#############
# Main Code #
#############
cat /proc/mdstat | grep -oP "md\d*" | while read line ; do
    if [[ ! $(mdadm --detail "/dev/$line" | grep -P "$regexQuery") ]]; then
        echo "$line has a problem! $(mdadm --detail "/dev/$line" | grep "State : " | sed "s/^ *//g"). For more info run: mdadm --detail /dev/$line"
	else
		if [[ "$1" = "-v" ]] || [[ "$1" = "--verbose" ]]; then
			echo "$line is fine. $(mdadm --detail "/dev/$line" | grep "State : " | sed "s/^ *//g")"
		fi
    fi
done
