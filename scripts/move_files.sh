#!/bin/bash

SOURCE_DIR="/data/receivearea"
DEST_DIR="/data/archievearea"

# Check if source directory exists
cmd=`pwd`

# Move files from source to destination
mv "${cmd}${SOURCE_DIR}"/* "${cmd}${DEST_DIR}"

# Check if the move was successful
if [ $? -eq 0 ]; then
  echo "Files successfully moved from $SOURCE_DIR to $DEST_DIR"
else
  echo "Error occurred while moving files"
  exit 1
fi
