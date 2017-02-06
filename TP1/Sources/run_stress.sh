#!/bin/bash
# Base on article https://la-vache-libre.org/stress-ng-un-outil-pratique-pour-tester-la-stabilite-des-composants-de-votre-machine-en-charge-elevee/

while getopts n:r: option
do
        case "${option}"
        in
                n) WORKER_COUNT=$OPTARG;;
                r) RESULT=$OPTARG;;
        esac
done

stress-ng --vm $WORKER_COUNT --timeout 10 --metrics-brief > $RESULT.txt
