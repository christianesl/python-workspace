#!/bin/bash

files= "file.txt file2.tx"
echo $files
for file in $files; do
	echo processing "~/data/f$file"
	if test -e ~/data/$file; then echo ~/data/$file >> oldFiles.txt;
	else echo "not exist";
	fi
done