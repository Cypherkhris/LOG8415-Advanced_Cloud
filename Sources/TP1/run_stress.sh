#!/bin/bash
# Base on article https://la-vache-libre.org/stress-ng-un-outil-pratique-pour-tester-la-stabilite-des-composants-de-votre-machine-en-charge-elevee/

while getopts r: option
do
        case "${option}"
        in
                r) RESULT=$OPTARG;;
        esac
done

stress-ng --vm 1 --metrics-brief > $RESULT.txt
