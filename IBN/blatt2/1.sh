#! /usr/bin/bash

# directory path as input, non-directory path rejected with an error message
if [ ! -d $1 ]; then
  echo "invalid directory '$1'"
  exit
fi

cd $1   # for convenience, has no effect after the script terminates

# list the contents recursively | keep only image files | go through the image files
ls -R | grep -E "\.(jpe?g|png)$"  | while read file; do                
		
		# get the name of the subdirectory by using the last modified date of the 
		# file, and formatting it
		subdir=$(date -r "$file" "+%Y-%m")

		# only create the subdirectory if it doesn't exist
		if [ ! -d $subdir ]; then
		   mkdir $subdir
		fi

		# move the file to the subridectory
		mv "$file" $subdir
	
	done
