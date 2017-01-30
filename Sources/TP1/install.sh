#!/bin/bash

# Check if root
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi

### Create folder to output result ###
mkdir result


### Install dependency to run test ###

# For the IOPS
apt-get install bonnie++

# For the Memory
apt-get install stress-ng