#!/usr/bin/env python

# CPU benchmarking

import subprocess
from utils import extractResult

def main(option, outputDirectory, fileName):
    command = "sysbench --test=cpu --cpu-max-prime=" + str(option) + " run"
    path = outputDirectory + "/" + fileName + ".txt"
    file = open(path, 'a')
    subprocess.call(command, shell=True, stdout=file)
    file.close()

def getResult(outputDirectory, fileName):

    regexPattern = r'([0-9]*\.[0-9]*)s'
    matchObjList = extractResult(outputDirectory, fileName, regexPattern)

    result = "Total time (s): {}".format(matchObjList[0].group(1))

    return "{}".format(result)