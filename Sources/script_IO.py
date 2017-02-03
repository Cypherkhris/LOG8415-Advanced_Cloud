#!/usr/bin/env python

# IO benchmarking

import subprocess
from utils import checkDirectory


def main(bs, count, outputDirectory, fileName):
    checkDirectory(outputDirectory)
    command = "dd if=/dev/zero of=sb-io-test bs=" + str(bs) + " count=" + str(count) + " conv=fdatasync"
    path = outputDirectory + "/" + fileName + ".txt"
    file = open(path, 'a')
    subprocess.call(command, shell=True, stderr=file)
    file.close()

if __name__ == '__main__':
    main()
