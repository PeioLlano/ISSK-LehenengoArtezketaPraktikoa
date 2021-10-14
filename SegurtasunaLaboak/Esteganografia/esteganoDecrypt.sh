#!/bin/bash

md5="e5ed313192776744b9b93b1320b5e268";
> zuzenak.txt;
		
for FILE in irudia/*.jpg;
do	
	if [ "$md5  $FILE" == "$(md5sum $FILE)" ];
	then
		echo "$FILE" >> zuzenak.txt;
	fi
done
