#!/usr/bin/python
"""Python module that sends TCP requests to AWS instance."""

import socket
import ConfigParser
from time import sleep


def main():
    """Main."""

    """Load config"""
    config = ConfigParser.ConfigParser()
    config.readfp(open(r'cluster.config'))

    listenPort = int(config.get('GateKeeper', 'port'))
    target = config.get('GateKeeper', 'target')
    targetHost = config.get(target, 'host')
    targetPort = int(config.get(target, 'port'))

    print 'Will listen to '+ str(listenPort)
    print 'Will send to ' + targetHost + ':' + str(targetPort)

    sendingSocket = socket.socket()
    sendingSocket.connect((targetHost, targetPort))

    listeningSocket = socket.socket()
    listeningSocket.bind(('', listenPort))
    listeningSocket.listen(1)
    c, addr = listeningSocket.accept()

    while True:
        data = c.recv(2048)

        if not data:
            break

        print 'Will pass data'

        data = str(data)

        """ Sending data """
        sendingSocket.send(data)
        response = sendingSocket.recv(1024)

        print 'Data sent'

        c.send(response)

    print 'Will close socket'
    sendingSocket.close()
    listeningSocket.close()


if __name__ == '__main__':
    main()
