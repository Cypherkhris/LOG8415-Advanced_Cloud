#!/usr/bin/env python

# CPU benchmarking

import subprocess

def main(option, outputDirectory, fileName):
    command = "sysbench --test=cpu --cpu-max-prime=" + str(option) + " run"
    path = outputDirectory + "/" + fileName + ".txt"
    file = open(path, 'a')
    subprocess.call(command, shell=True, stdout=file)
    file.close()


