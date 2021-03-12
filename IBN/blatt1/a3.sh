#! /usr/bin/bash

if [ ! -d $1 ]; then
	echo "argument '$1' is invalid"
	exit
fi

echo "5 biggest files in $1"
ls $1 -Sp | grep -v / | head -5

sleep 5

echo "5 last modified files starting with '$2' in $1"
ls $1 -tp | grep -v / | grep ^$2 | head -5




