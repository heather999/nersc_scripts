#!/bin/bash

#find $1 -maxdepth 2 -name postISRCCD -exec rm -rf {} + 
find coadd-v1/deepCoadd -maxdepth 4 -name "[0-9],[0-9]" -exec rm -rf {} +

