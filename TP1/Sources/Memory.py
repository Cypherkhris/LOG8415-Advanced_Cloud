#!/usr/bin/env python

# IO benchmarking

import subprocess

def test():
    runMemoryBenchmark(1, "result", "memory")


def runMemoryBenchmark(memorySize, outputDirectory, fileName):

    subprocess.call("./run_stress.sh -n {} -r {}/{}".format(memorySize, outputDirectory, fileName), shell=True)
