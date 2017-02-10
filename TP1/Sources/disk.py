#!/usr/bin/env python

# IO benchmarking

import subprocess
import os
from utils import extractResult


def test():
    runDiskBenchmark("result" ,"disk", "/sda/dev")

def runDiskBenchmark(outputDirectory, fileName, ./pudiskMount):

    subprocess.call("./run_disk.sh -r {}/{}".format( outputDirectory, fileName), shell=True)


def getResult(outputDirectory, fileName):

    regexPattern = r'([0-9]*\.[0-9]*) MB\/sec'
    matchObjList = extractResult(outputDirectory, fileName, regexPattern)

    cachedPerformance = "Cached reads: {}".format(matchObjList[0].group(1))
    bufferedPerformance = "Buffered reads: {}".format(matchObjList[1].group(1))

    return "{}, {}".format(cachedPerformance, bufferedPerformance)