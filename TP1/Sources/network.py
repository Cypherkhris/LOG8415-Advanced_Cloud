#!/usr/bin/env python

# IO benchmarking

import subprocess
from utils import extractResult

def test():
    runNetworkBenchmark("result" ,"network")

def runNetworkBenchmark(outputDirectory, fileName):

    subprocess.call("./run_network.sh -r {}/{}".format( outputDirectory, fileName), shell=True)



def getResult(outputDirectory, fileName):

    regexPattern = r'([0-9]*\.[0-9]*) Mbit\/s'
    matchObjList = extractResult(outputDirectory, fileName, regexPattern)

    downloadSpeed = "Download speed (Mb/s): {}".format(matchObjList[0])
    uploadSpeed = "Upload speed (Mb/s): {}".format(matchObjList[1])

    return "{}, {}".format(downloadSpeed, uploadSpeed)
