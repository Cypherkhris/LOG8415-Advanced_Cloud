#!/bin/bash
# Base on article http://support.commgate.net/index.php?/Knowledgebase/Article/View/

while getopts d:m:r: option
do
        case "${option}"
        in
                d) DIR=$OPTARG;;
                m) MEMORY=$OPTARG;;
                r) RESULT=$OPTARG;;
        esac
done

bonnie++ -d $DIR -r $MEMORY | bon_csv2html > $RESULT.html
