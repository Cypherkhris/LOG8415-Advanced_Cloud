#!/bin/bash
# Base on article http://support.commgate.net/index.php?/Knowledgebase/Article/View/


while getopts d:r:f: option
do
        case "${option}"
        in
                d) DIR=${OPTARG};;
                r) RAM=${OPTARG};;
                o) OUTPUT=$OPTARG;;
        esac
done


bonnie++ -d $DIR -r $RAM -u root | bon_csv2html > $OUTPUT.html