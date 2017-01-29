#!/usr/bin/env python

# CPU benchmarking

import subprocess

def main(option):
    command = "sysbench --test=cpu --cpu-max-prime=" + str(option) + " run"
    subprocess.call(command, shell=True)

if __name__ == '__main__':
    main()

