#!/usr/bin/env python

# IO benchmarking

import subprocess
from utils import checkDirectory


def main(bs, count, outputDirectory, fileName):
    checkDirectory(outputDirectory)
    command = "dd if=/dev/zero of=sb-io-test bs=" + str(bs) + " count=" + str(count) + " conv=fdatasync"
    path = outputDirectory + "/" + fileName + ".txt"
    file = open(path, 'w')
    subprocess.call(command, shell=True, stdout=file)
    file.close()

if __name__ == '__main__':
    main()
