#!/bin/bash

if [ ! -d backup ]; then
		mkdir backup
		echo "Directory $backup created!"
fi

cp data/*.txt backup/

echo "Backup Completed!"
