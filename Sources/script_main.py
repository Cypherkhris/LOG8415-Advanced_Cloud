#!/usr/bin/env python

# Script principal
# "For each instance type, you should execute your selected benchmarks at least 5 times and take the average."

import script_CPU
import script_IO
import sys
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cpu', dest='cpu', help='SysBench cpu-max-prime option')
    parser.add_argument('--bs', dest='bs', help='dd bs option')
    parser.add_argument('--count', dest='count', help='dd count option')
    options = parser.parse_args()
    if options.cpu is None:
        options.cpu = '20000'
    if options.bs is None:
        options.bs = '1M'
    if options.count is None:
        options.count = '1k'

    print '\nSTARTING CPU BENCHMARKING \n'
    script_CPU.main(options.cpu, "result", "cpu")

    print '\nSTARTING IO BENCHMARKING \n'
    script_IO.main(options.bs, options.count, "result", "io")

if __name__ == '__main__':
    main()
