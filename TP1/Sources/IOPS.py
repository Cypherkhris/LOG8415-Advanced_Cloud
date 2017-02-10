#!/usr/bin/env python

# IO benchmarking

import subprocess
from utils import checkDirectory

def test():
    runIopsBenchmark("test", 2048, "result", "iops")

def runIopsBenchmark(testDirectoryPath, ramSize, outputDirectory, fileName):

    checkDirectory(testDirectoryPath)

    subprocess.call("./run_bonnie.sh -d {} -m {} -r {}/{}".format(testDirectoryPath, ramSize, outputDirectory, fileName), shell=True)


def getResult(outputDirectory, fileName):

    return "too lazy go check html"