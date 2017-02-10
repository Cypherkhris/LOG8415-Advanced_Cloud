#!/usr/bin/env python

# IO benchmarking

import subprocess
from utils import extractResult

def test():
    runMemoryBenchmark(1, "result", "memory")


def runMemoryBenchmark(memorySize, outputDirectory, fileName):

    subprocess.call("./run_stress.sh -n {} -r {}/{}".format(memorySize, outputDirectory, fileName), shell=True)

def getResult(outputDirectory, fileName):

    regexPattern = r'([0-9]*\.[0-9]*) *([0-9]*\.[0-9]*)$'
    matchObjList = extractResult(outputDirectory, fileName, regexPattern)

    performance = "Bogo (real time, total) : {} ops/s".format(matchObjList[0])

    return "{}".format(performance)
