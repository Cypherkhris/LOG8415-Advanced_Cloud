#!/usr/bin/env python

# Script principal
# "For each instance type, you should execute your selected benchmarks at least 5 times and take the average."

import argparse

import script_CPU
import script_IO
import IOPS
import Memory
import disk
import network

from utils import checkDirectory




def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cpu', dest='cpu', help='SysBench cpu-max-prime option')
    parser.add_argument('--bs', dest='bs', help='dd bs option')
    parser.add_argument('--count', dest='count', help='dd count option')
    parser.add_argument('--ram', dest='ram', help='RAM size for IOPS benchmark')
    parser.add_argument('--memory', dest='memory', help='Gig size of virtual memory for memory benchmark')
    parser.add_argument('--provider', dest='provider', help='Gig size of virtual memory for memory benchmark')
    options = parser.parse_args()
    if options.cpu is None:
        options.cpu = '20000'
    if options.bs is None:
        options.bs = '1M'
    if options.count is None:
        options.count = '1k'
    if options.ram is None:
        options.ram = 1024
    if options.memory is None:
        options.memory = 1
    if options.provider is None:
        options.provider = "azure"

    resultDirectory = "result"

    checkDirectory(resultDirectory)

    results = []

    results.append("Result for command --cpu {} -- bs {}  -- count {} -- ram {} --memory {}  --provider {}".format(options.cpu, options.bs, options.count, options.ram, options.memory, options.provider))

    print '\nSTARTING CPU BENCHMARKING \n'

    script_CPU.main(options.cpu, resultDirectory, "cpu")
    results.append("CPU: " + script_CPU.getResult(resultDirectory, "cpu.txt"))

    print '\nSTARTING IO BENCHMARKING \n'

    script_IO.main(options.bs, options.count, resultDirectory, "io")
    results.append("IO: " + script_IO.getResult(resultDirectory, "io.txt"))

    print '\nSTARTING IOPS BENCHMARKING \n'

    IOPS.runIopsBenchmark("test", options.ram, resultDirectory, "iops")
    results.append("IOPS: " + IOPS.getResult(resultDirectory, "iops.txt"))

    print '\nSTARTING MEMORY BENCHMARKING \n'

    Memory.runMemoryBenchmark(options.memory, resultDirectory, "memory")
    results.append("Memory: " + Memory.getResult(resultDirectory, "memory.txt"))

    print '\nSTARTING DISK BENCHMARKING \n'

    diskMount = "/xdva/xdva" if options.provider == "azure" else "/dev/sda"
    disk.runDiskBenchmark(resultDirectory, "disk", diskMount)
    results.append("Disk: " + disk.getResult(resultDirectory, "disk.txt"))

    print '\nSTARTING NETWORK BENCHMARKING \n'

    network.runNetworkBenchmark(resultDirectory, "network")
    results.append("Network: " + network.getResult(resultDirectory, "network.txt"))

    resultFile = open(resultDirectory + "/resultCompilation.txt", "w")
    
    for item in results:
        resultFile.write("%s\n" %item)


if __name__ == '__main__':
    main()
