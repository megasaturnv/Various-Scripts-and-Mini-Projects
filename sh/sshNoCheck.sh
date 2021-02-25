#!/bin/sh
#MegaSaturnv 2017-07-28
#SSH without checking known hosts file 
alias sshNoCheck='ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no'