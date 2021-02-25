#!/bin/sh
#MegaSaturnv 2017-11-17
#Setup a custom tmux session

#Useful examples: /usr/share/doc/tmux/examples

SESSION="tmux_$USER"

tmux -2 new-session -d -s $SESSION

#0 Setup a window for general use
tmux rename-window -t $SESSION:0 "General"
tmux send-keys "cd $HOME" C-m

#1 Setup a window for Desktop
tmux new-window -t $SESSION:1 -n "Desktop"
tmux split-window -h
tmux select-pane -t 0
tmux send-keys "clear && cd $HOME && ll" C-m
tmux select-pane -t 1
tmux send-keys "clear && cd $HOME/Desktop && ll" C-m
tmux select-pane -t 0

#2 Setup a window for python
tmux new-window -t $SESSION:2 -n "Python"
tmux split-window -v
tmux select-pane -t 1
tmux resize-pane -D 15
#tmux resize-pane -D -y 8
tmux select-pane -t 0
tmux send-keys "clear && cd $HOME && ll" C-m
tmux select-pane -t 1
tmux send-keys "clear && cd $HOME && python3" C-m
tmux select-pane -t 0

#3 Setup a window for tailing log files
tmux new-window -t $SESSION:3 -n "Logs"
tmux split-window -v
tmux select-pane -t 0
tmux resize-pane -D 20
tmux send-keys "clear && cd /var/log & ls" C-m
tmux select-pane -t 1
tmux send-keys "clear && cd /var/log/apache2 & ls" C-m
tmux select-pane -t 0

#4 Setup a window for ssh
tmux new-window -t $SESSION:4 -n "SSH"
tmux send-keys "cd $HOME && clear" C-m

tmux select-window -t $SESSION:0

tmux -2 attach-session -t $SESSION