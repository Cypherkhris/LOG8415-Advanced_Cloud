#!/usr/bin/env python

# IO benchmarking

import subprocess


def main(bs, count):
    command = "dd if=/dev/zero of=sb-io-test bs=" + str(bs) + " count=" + str(count) + " conv=fdatasync"
    subprocess.call(command, shell=True)

if __name__ == '__main__':
    main()
