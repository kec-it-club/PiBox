#!/bin/sh

piBox/__init__.py &
ID=$!
sleep 0.25
piBrowser/pibrowser.py
kill $ID