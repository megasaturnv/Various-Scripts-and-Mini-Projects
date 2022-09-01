#!/bin/bash

if [ -z "$*" ]; then
    echo 'Usage: ./pairGoPro.sh <pin>'
elif [[ $1 == '-h' ]]; then
    echo 'Usage: ./pairGoPro.sh <pin>'
else
	curl "https://10.5.5.9/gpPair?c=start&pin=$1&mode=0"
	sleep 1
	curl "https://10.5.5.9/gpPair?c=finish&pin=$1&mode=0"

	echo "Pair complete!"
fi
