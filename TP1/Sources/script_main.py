#!/usr/bin/env python

# Script principal
# "For each instance type, you should execute your selected benchmarks at least 5 times and take the average."

import argparse

import script_CPU
import script_IO
from IOPS import runIopsBenchmark
from Memory import runMemoryBenchmark
from disk import runDiskBenchmark
from network import runNetworkBenchmark
from utils import checkDirectory


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cpu', dest='cpu', help='SysBench cpu-max-prime option')
    parser.add_argument('--bs', dest='bs', help='dd bs option')
    parser.add_argument('--count', dest='count', help='dd count option')
    parser.add_argument('--ram', dest='ram', help='RAM size for IOPS benchmark')
    parser.add_argument('--worker', dest='worker', help='Worker count for memory benchmark')
    options = parser.parse_args()
    if options.cpu is None:
        options.cpu = '20000'
    if options.bs is None:
        options.bs = '1M'
    if options.count is None:
        options.count = '1k'
    if options.ram is None:
        options.ram = 1024
    if options.worker is None:
        options.worker = 1

    resultDirectory = "result"

    checkDirectory(resultDirectory)

    print '\nSTARTING CPU BENCHMARKING \n'
    script_CPU.main(options.cpu, resultDirectory, "cpu")

    print '\nSTARTING IO BENCHMARKING \n'
    script_IO.main(options.bs, options.count, resultDirectory, "io")

    print '\nSTARTING IOPS BENCHMARKING \n'
    runIopsBenchmark("test", options.ram, resultDirectory, "iops")

    print '\nSTARTING MEMORY BENCHMARKING \n'
    runMemoryBenchmark(options.worker, resultDirectory, "memory")

    print '\nSTARTING DISK BENCHMARKING \n'
    runDiskBenchmark(resultDirectory, "disk")

    print '\nSTARTING DISK NETWORK \n'
    runNetworkBenchmark(resultDirectory, "network")


if __name__ == '__main__':
    main()
