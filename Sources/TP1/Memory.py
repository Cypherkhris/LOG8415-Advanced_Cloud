#!/usr/bin/env python

# IO benchmarking

import subprocess
from utils import checkDirectory

def test():
    runStress(1, "result", "memory")


def runStress(workerCount, outputDirectory, fileName):

    checkDirectory(outputDirectory)

    subprocess.call("./run_stress.sh -n {} -r {}/{}".format(workerCount, outputDirectory, fileName), shell=True)
