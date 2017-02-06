#!/bin/bash
# Base on article http://support.commgate.net/index.php?/Knowledgebase/Article/View/

# Check if root
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi

while getopts r: option
do
        case "${option}"
        in
                r) RESULT=$OPTARG;;
        esac
done

hdparm -Tt /dev/sda > $RESULT.txt
