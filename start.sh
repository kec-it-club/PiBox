#!/bin/sh

DIR=$( cd "$(dirname $0)" && pwd )
$DIR/piBox/__init__.py &
ID=$!
sleep 0.25
$DIR/piBrowser/pibrowser.py
kill $ID
