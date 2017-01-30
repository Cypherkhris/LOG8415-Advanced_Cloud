#!/usr/bin/env python

# IO benchmarking

import subprocess


def runBonnie(testDirectoryPath, ramSize, outputPath, fileName):
    subprocess.call("./bonnie -d {} -r {} -o {}{}".format(testDirectoryPath, ramSize, outputPath, fileName), shell=True)
