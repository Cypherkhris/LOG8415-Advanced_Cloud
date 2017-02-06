#!/bin/bash

# Check if root
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi

### Create folder to output result ###
mkdir -m 777 result


### Install dependency to run test ###

# For the CPU
apt-get install sysbench

# For the IOPS
apt-get install bonnie++
chmod +x run_bonnie.sh

# For the Memory
apt-get install stress-ng
chmod +x run_stress.sh

# For Disk
apt-get install hdparm
chmod +x run_disk.sh

# For network
apt-get install speedtest-cli
chmod +x run_network