#!/usr/bin/env python

# CPU benchmarking

import subprocess

def main():
    subprocess.call("sysbench --test=cpu --cpu-max-prime=20000 run", shell=True)

if __name__ == '__main__':
    main()

