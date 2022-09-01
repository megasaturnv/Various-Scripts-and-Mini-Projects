#!/bin/bash

# Usage: ./ffmpeg_clip.sh <filename> <start mm:ss> <end mm:ss>
# Example: ./ffmpeg_clip.sh file.mp4 01:15 01:45
# Output file is <filename>_clip.mp4

FILE=$1
START_TIME=$2
END_TIME=$3

echo "start $(date -Iseconds)"

#Don't rotate 180
ffmpeg -hide_banner -loglevel error -i "$1" -ss "$START_TIME" -to "$END_TIME" -metadata:s:v rotate=0 -codec:v libx264 -codec:a aac "$1_clip.mp4"
# ffmpeg -hide_banner -loglevel error -i "$1" -ss "$START_TIME" -to "$END_TIME" -metadata:s:v rotate=0 -codec:v copy -codec:a aac "$1_clip.mp4"
# ffmpeg -hide_banner -loglevel error -i "$1" -ss "$START_TIME" -to "$END_TIME" -metadata:s:v rotate=0 -codec:v copy -codec:a copy "$1_clip.mp4"

#Rotate 180
#ffmpeg -hide_banner -loglevel error -i "$1" -ss "$START_TIME" -to "$END_TIME" -vf "transpose=2,transpose=2,format=yuv420p" -metadata:s:v rotate=0 -codec:v libx264 -codec:a aac "$1_clip.mp4"

#Rotate 180 Alternate method
#ffmpeg -hide_banner -loglevel error -i "$1" -ss "$START_TIME" -to "$END_TIME" -vf "rotate=PI:bilinear=0,format=yuv420p" -metadata:s:v rotate=0 -codec:v libx264 -codec:a aac "$1_clip2.mp4"

echo "end $(date -Iseconds)"
