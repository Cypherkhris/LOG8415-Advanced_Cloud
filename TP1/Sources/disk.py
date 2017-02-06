#!/usr/bin/env python

# IO benchmarking

import subprocess
import os
from utils import checkDirectory

def test():
    runDiskBenchmark("result" ,"disk")

def runDiskBenchmark(outputDirectory, fileName):

    subprocess.call("./run_disk.sh -r {}/{}".format( outputDirectory, fileName), shell=True)
