#!/bin/bash
# Base on article http://support.commgate.net/index.php?/Knowledgebase/Article/View/

# Check if root
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi

while getopts d:m:r: option
do
        case "${option}"
        in
                d) DIR=$OPTARG;;
                m) MEMORY=$OPTARG;;
                r) RESULT=$OPTARG;;
        esac
done

bonnie++ -d $DIR -r $MEMORY -u 0 | bon_csv2html > $RESULT.html
