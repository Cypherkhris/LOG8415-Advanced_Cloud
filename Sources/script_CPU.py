#!/usr/bin/env python

# CPU benchmarking

import subprocess
from utils import checkDirectory


def main(option, outputDirectory, fileName):
    checkDirectory(outputDirectory)
    command = "sysbench --test=cpu --cpu-max-prime=" + str(option) + " run"
    path = outputDirectory + "/" + fileName + ".txt"
    file = open(path, 'a')
    subprocess.call(command, shell=True, stdout=file)
    file.close()

if __name__ == '__main__':
    main()

