#!/usr/bin/env python

import subprocess
import argparse

# inspired by https://www.cyberciti.biz/faq/linux-ram-info-command/ and https://en.wikipedia.org/wiki/Hdparm

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', dest='path', help='Path for the output file')
    parser.add_argument('--interface', dest='interfaceName', help='Interface name for the network information')
    options = parser.parse_args()

    command_HD = "sudo hdparm -I /dev/sda" # get hard drive info
    command_mem = "free -h" # get memory size
    command_mem2 = "dmidecode --type 17" # get memory speed -- 17 is SMIBIOS code for 'Memory Device' type
    command_CPU = "cat /proc/cpuinfo" # get CPU info
    command_net = "ethtool " + options.interfaceName # get network info -- get interface name from 'ifconfig'

    file = open(options.path, 'a')
    subprocess.call("echo '#### CPU info #### \n'", shell=True, stdout=file)
    subprocess.call(command_CPU, shell=True, stdout=file)
    subprocess.call("echo '\n \n#### memory size #### \n'", shell=True, stdout=file)
    subprocess.call(command_mem, shell=True, stdout=file)
    subprocess.call("echo '\n \n#### memory info #### \n'", shell=True, stdout=file)
    subprocess.call(command_mem2, shell=True, stdout=file)
    subprocess.call("echo '\n \n#### disk info #### \n'", shell=True, stdout=file)
    subprocess.call(command_HD, shell=True, stdout=file)
    subprocess.call("echo '\n \n#### network info #### \n'", shell=True, stdout=file)
    subprocess.call(command_net, shell=True, stdout=file)
    file.close()

if __name__ == '__main__':
    main()

