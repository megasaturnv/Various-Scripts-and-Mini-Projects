#!/bin/sh
#MegaSaturnv 2017-11-17
#Automatically attach to a tmux session if one exists
(tmux ls | grep -q "attached" && echo "[Info] You are already attached to a tmux session") || tmux attach