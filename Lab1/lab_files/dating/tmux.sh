#!/bin/bash
# Install tmux
apt-get install -y tmux

# Start new tmux session unattached
tmux new-session -d -s "triple"

# Split twice
tmux split-window -h
tmux split-window -h

# Balance panes
tmux select-layout even-horizontal

# Attach terminal
tmux a -t "triple"