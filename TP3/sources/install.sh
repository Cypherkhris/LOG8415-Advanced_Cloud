#!/bin/bash

# Check if root
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi


### Set script executatble

chmod +x *.py

### Install dependency to run test ###

# For the CPU
apt-get install fping