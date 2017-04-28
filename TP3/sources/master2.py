#!/usr/bin/python
"""Python module that receives TCP requests."""

import socket
import pickle
import ConfigParser
from random import randint
from pingHelper import get_ping_time



"""Load config"""
clusterConfig = ConfigParser.ConfigParser()
clusterConfig.readfp(open(r'cluster.config'))

port = int(clusterConfig.get("Master", 'port'))



def main():
    """Main."""
    s = socket.socket()
    s.bind(('', port))

    print 'Listening port : ' + str(port)

    s.listen(1)  # Listen to one connection
    c, addr = s.accept()
    print 'connection from: ' + str(addr)

    while True:
        obj = pickle.load(c)
        print 'target = ' + obj['target']
        print 'command = ' + obj['command']
        # data = c.recv(2048)  # Max bytes
        # if not data:
        #     break
        #
        # print 'from connected user: ' + str(data)
        # data = str(data)

        # response = 'Command of type ' + type + ' handle by node ' + str(target)
        #response = 'received' + data
        response = 'ok'
        c.send(response)

    print 'Will close socket'
    c.close()

def my_pattern():
    """Implement algorithm of the pattern here."""
    # Connect to MySQL Cluster
    # Hit the database based on the algorithm
    # TO DO ...


if __name__ == '__main__':
    main()
