#!/usr/bin/env python

# IO benchmarking

import subprocess


def test():
    runNetworkBenchmark("result" ,"network")

def runNetworkBenchmark(outputDirectory, fileName):

    subprocess.call("./run_network.sh -r {}/{}".format( outputDirectory, fileName), shell=True)
