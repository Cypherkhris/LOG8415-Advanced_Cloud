#!/bin/bash
# inspired by https://stackoverflow.com/questions/13356628/is-there-a-way-to-redirect-time-output-to-file-in-linux

echo 'PROCESS START'
while getopts o: option
do
        case "${option}"
        in
                o) DIR=$OPTARG;;
        esac
done

{ time hadoop jar /usr/local/hadoop-2.7.3/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.3.jar wordcount input/ulysses.txt output/$DIR/ 2> hadoop.stderr ; } 2>> time_script.txt
echo 'PROCESS END'
