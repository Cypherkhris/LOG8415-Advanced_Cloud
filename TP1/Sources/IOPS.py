#!/usr/bin/env python

# IO benchmarking

import subprocess
import os
from utils import checkDirectory

def test():
    runIopsBenchmark("test", 2048, "result", "iops")

def runIopsBenchmark(testDirectoryPath, ramSize, outputDirectory, fileName):

    checkDirectory(testDirectoryPath)
    checkDirectory(outputDirectory)

    subprocess.call("./run_bonnie.sh -d {} -m {} -r {}/{}".format(testDirectoryPath, ramSize, outputDirectory, fileName), shell=True)
