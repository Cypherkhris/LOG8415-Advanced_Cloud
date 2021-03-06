#!/usr/bin/python
"""Python module that sends TCP requests to AWS instance."""

import socket
import pickle
import ConfigParser
from time import sleep


insert = 'INSERT INTO transactions VALUES ('
select = 'SELECT * FROM transactions WHERE serial = '



def main():
    """Main."""

    """Load config"""
    config = ConfigParser.ConfigParser()
    config.readfp(open(r'cluster.config'))
    target = config.get('Client', 'target')
    host = config.get(target, 'host')
    port = int(config.get(target, 'port'))

    print 'Will connect to ' + host + ':' + str(port)

    s = socket.socket()
    s.connect((host, port))



    with open('data/data_dump.csv', 'r') as f:
        lines = f.readlines()
        do_insert = True;
        cmd_type = 'insert'
        for line in lines:
            line = line.strip('\n')
            print line
            member_id, date, country, gender, ip_address, amount, vip, product_id, card_type, serial, zone = line.split(",")
            if(do_insert):
                cmd = insert + member_id + ", '" + date + "', '" + country + "', '" + gender + "', '" + ip_address + "', " + amount + ", " + vip + ", " + product_id + ", '" + card_type + "', '" + serial + "', '" + zone + "');"
                do_insert = False;
                cmd_type = 'insert'
            else:
                cmd = select + "'" + serial + "';"
                do_insert = True;
                cmd_type = 'select'
            if target == 'Master':
                obj = {'target': '', 'type': cmd_type, 'command': cmd}
                pickledobj = pickle.dumps(obj)
                s.send(pickledobj)
            else:
                s.send(cmd)
            data = s.recv(1024)
            print 'Received from server: ' + str(data)

    print 'Will close socket'
    s.close()


if __name__ == '__main__':
    main()
