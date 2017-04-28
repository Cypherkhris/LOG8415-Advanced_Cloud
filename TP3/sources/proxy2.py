#!/usr/bin/python
"""Python module that receives and sends TCP requests."""

import socket
import pickle
import ConfigParser
from random import randint
from pingHelper import get_ping_time



"""Load config"""
config = ConfigParser.ConfigParser()
config.readfp(open(r'cluster.config'))

listenPort = int(config.get("Proxy", 'port'))
slaveCount = int(config.get('ClusterInfo', 'slaveCount'))
mode = config.get('ProxyInfo', 'mode')
pingCount = int(config.get('ProxyInfo', 'pingCount'))
target = config.get('Proxy', 'target')
targetHost = config.get(target, 'host')
targetPort = int(config.get(target, 'port'))



def main():
    """Main."""
    sendingSocket = socket.socket()
    sendingSocket.connect((targetHost, targetPort))

    listeningSocket = socket.socket()
    listeningSocket.bind(('', listenPort))
    print 'Listening port : ' + str(listenPort)
    listeningSocket.listen(1)
    c, addr = listeningSocket.accept()

    print 'connection from: ' + str(addr)

    while True:
        data = c.recv(2048)  # Max bytes
        if not data:
            break

        print 'from connected user: ' + str(data)
        data = str(data)

        type, command = parse_data(data)

        target = get_target()

        obj = {'target': target, 'command': command}
        pickle.dump(obj, sendingSocket)

        # req = 'Command of type ' + type + ' handle by node ' + str(target)
        # sendingSocket.send(req)
        response = sendingSocket.recv(1024)
        print 'Data sent'

        c.send(response)

    print 'Will close socket'
    sendingSocket.close()
    listeningSocket.close()


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
    selectedSlave = 0
    minTiming = 999999

    for slaveIndex in range (0, slaveCount):
        slaveConfigName = 'Slave' + str(slaveIndex)
        host = config.get(slaveConfigName, 'host')
        time = get_ping_time(host, pingCount)
        print 'Slave-' + str(slaveIndex) + ' timing: ' + str(time)
        if time < minTiming:
            minTiming = time
            selectedSlave = slaveIndex

    return selectedSlave


if __name__ == '__main__':
    main()
