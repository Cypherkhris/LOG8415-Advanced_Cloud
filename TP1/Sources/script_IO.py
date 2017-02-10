#!/usr/bin/env python

# IO benchmarking

import subprocess
from utils import extractResult

def main(bs, count, outputDirectory, fileName):
    command = "dd if=/dev/zero of=sb-io-test bs=" + str(bs) + " count=" + str(count) + " conv=fdatasync"
    path = outputDirectory + "/" + fileName + ".txt"
    file = open(path, 'a')
    subprocess.call(command, shell=True, stderr=file)
    file.close()

def getResult(outputDirectory, fileName):

    regexPattern = r'([0-9]*\.?[0-9]*) MB\/s'
    matchObjList = extractResult(outputDirectory, fileName, regexPattern)

    result = "Speed (MB/s): {}".format(matchObjList[0].group(1))

    return "{}".format(result)