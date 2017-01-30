#!/usr/bin/env python

# IO benchmarking

import subprocess
import os
from utils import checkDirectory

def test():
    runStress("result", "memory")


def runStress(outputDirectory, fileName):

    checkDirectory(outputDirectory)

    subprocess.call("./run_stress.sh -r {}/{}".format(outputDirectory, fileName), shell=True)
