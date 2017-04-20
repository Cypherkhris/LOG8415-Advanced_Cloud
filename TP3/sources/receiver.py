#!/usr/bin/python
"""Python module that receives TCP requests."""

import socket
import ConfigParser
from random import randint


port = 5001

"""Load config"""
modeConfig = ConfigParser.ConfigParser()
modeConfig.readfp(open(r'mode.config'))
mode = modeConfig.get('ProxyMode', 'mode')

clusterConfig = ConfigParser.ConfigParser()
clusterConfig.readfp(open(r'cluster.config'))
slaveCount = clusterConfig.get('ClusterInfo', 'slaveCount')




def main():
    """Main."""
    s = socket.socket()
    s.bind(('', port))

    print 'Listening port : ' + str(port)

    s.listen(1)  # Listen to one connection
    c, addr = s.accept()
    print 'connection from: ' + str(addr)

    while True:
        data = c.recv(2048)  # Max bytes
        if not data:
            break

        print 'from connected user: ' + str(data)
        data = str(data)

        type, command = parse_data(data)

        target = get_target()

        # if type == 'insert':
        #     hit_master(command)
        # else:
        #   my_pattern(command)
        #

        response = 'Command of type ' + type + ' handle by node ' + str(target)
        c.send(response)

    # c.close()


def parse_data(data):
    """Function that takes the data and parses it."""
    type = 'select'

    if 'INSERT' in data:
        type = 'insert'

    command = data

    return type, command


def get_target():
    """
        0: master
        [1,...]: slave id
    """

    options = {
        'direct' : direct_mode,
        'random' : random_mode,
        'balancing' : balancing_mode
    }

    target = options[mode]()
    return target

def direct_mode():
    return 0

def random_mode():
    return randint(1, slaveCount)

def balancing_mode():
    return 0


def my_pattern():
    """Implement algorithm of the pattern here."""
    # Connect to MySQL Cluster
    # Hit the database based on the algorithm
    # TO DO ...


if __name__ == '__main__':
    main()
