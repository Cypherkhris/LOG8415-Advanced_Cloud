#!/usr/bin/python
"""Python module that receives TCP requests."""

import socket
import pickle
import mysql.connector
import ConfigParser
from random import randint
from pingHelper import get_ping_time



"""Load config"""
clusterConfig = ConfigParser.ConfigParser()
clusterConfig.readfp(open(r'cluster.config'))

port = int(clusterConfig.get("Master", 'port'))



def main():
    """Main."""
    # Initialisation de la connexion
    cnx = mysql.connector.connect(user='root', password='mtL86mLm', host='127.0.0.1', database='tp3')
    cursor = cnx.cursor()
    print 'Connection to DB opened'

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

        data = str(data)
        obj = pickle.loads(data)
        command = obj['command']
        cmd_type = obj['type']
        target = obj['target']

        print 'from connected user: ' + str(command) + ' to ' + str(target)

        if cmd_type == 'insert':
            cursor.execute(command)
            cnx.commit()
        else:
            cursor.execute(command)
            for (member_id, date, country, gender, ip_address, amount, vip, product_id, card_type, serial, zone) in cursor:
                print str(member_id) + 'is the winner'

        response = 'Command ' + command + ' handled by node ' + str(target)
        c.send(response)

    print 'Will close socket'
    c.close()
    print 'Will close connection to DB'
    cursor.close()
    cnx.close()

def my_pattern():
    """Implement algorithm of the pattern here."""
    # Connect to MySQL Cluster
    # Hit the database based on the algorithm
    # TO DO ...


if __name__ == '__main__':
    main()
