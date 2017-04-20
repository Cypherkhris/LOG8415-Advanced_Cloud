#!/usr/bin/python
"""Python module that sends TCP requests to AWS instance."""

import socket
import ConfigParser
from time import sleep


insert = 'INSERT INTO transactions VALUES ('
select = 'SELECT * FROM transactions WHERE serial = '



def main():
    """Main."""

    """Load config"""
    config = ConfigParser.ConfigParser()
    config.readfp(open(r'cluster.config'))
    host = config.get('Master', 'host')
    port = config.get('Master', 'port')



    s = socket.socket()
    s.connect((host, port))

    with open('data_dump.csv', 'r') as f:
        lines = f.readlines()
        do_insert = True;
        for line in lines:
            print line
            member_id, date, country, gender, ip_address, amount, vip, product_id, card_type, serial, zone = line.split(",")
            if(do_insert):
                cmd = insert + member_id + ", '" + date + "', '" + country + "', '" + gender + "', '" + ip_address + "', " + amount + ", " + vip + ", " + product_id + ", '" + card_type + "', '" + serial + "', '" + zone + "');"
                do_insert = False;
            else:
                cmd = select + "'" + serial + "';"
                do_insert = True;
            s.send(cmd)
            sleep(0.1)
            data = s.recv(1024)
            print 'Received from server: ' + str(data)

    s.close()


if __name__ == '__main__':
    main()
