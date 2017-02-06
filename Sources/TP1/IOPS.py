#!/usr/bin/env python

# IO benchmarking

import subprocess
import os
from utils import checkDirectory

def test():
    runBonnie("test", 2048, "result", "iops")

def checkDirectory(directoryPath):
    if not os.path.exists(directoryPath):
        os.makedirs(directoryPath)


def runBonnie(testDirectoryPath, ramSize, outputDirectory, fileName):

    checkDirectory(testDirectoryPath)
    checkDirectory(outputDirectory)

    subprocess.call("./run_bonnie.sh -d {} -m {} -r {}/{}".format(testDirectoryPath, ramSize, outputDirectory, fileName), shell=True)
