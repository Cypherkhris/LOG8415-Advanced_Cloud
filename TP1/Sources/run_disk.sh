#!/bin/bash
# Base on article http://support.commgate.net/index.php?/Knowledgebase/Article/View/

while getopts r: option
do
        case "${option}"
        in
                r) RESULT=$OPTARG;;
        esac
done

hdparm -Tt /dev/sda > $RESULT.txt
