#!/usr/bin/env python

# IO benchmarking

import subprocess


def main():
    subprocess.call("dd if=/dev/zero of=sb-io-test bs=1M count=1k conv=fdatasync", shell=True)

if __name__ == '__main__':
    main()
