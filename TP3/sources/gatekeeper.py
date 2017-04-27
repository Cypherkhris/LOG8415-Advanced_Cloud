#!/usr/bin/python
"""Python module that sends TCP requests to AWS instance."""

import socket
import ConfigParser
import re
from time import sleep

selectValidator = re.compile(r"(^select \* from transactions where serial = '\d{3}-\d{2}-\d{4}';)")
insertValidator = re.compile(r"(^insert into transactions values \([\w|\d|\s|,|'|\-|\.|\$]*\);$)")

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

        

        data = str(data)

        if(validate(data)):
            print 'Will pass data'

            """ Sending data """
            sendingSocket.send(data)
            response = sendingSocket.recv(1024)

            print 'Data sent'

            c.send(response)

        else:
            print 'Data denied'
            c.send('Invalid request')

    print 'Will close socket'
    sendingSocket.close()
    listeningSocket.close()


def validate(data):
    data = data.lower()
    print (data)
    if data.startswith('insert '):
        return bool(insertValidator.match(data))
    if data.startswith('select '):
        return bool(selectValidator.match(data))
    return False




if __name__ == '__main__':
    main()
