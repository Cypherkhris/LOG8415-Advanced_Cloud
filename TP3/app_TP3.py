#!/usr/bin/python
"""Python module that sends TCP requests to AWS instance."""

import socket
from time import sleep

host = 'ec2-52-89-34-120.us-west-2.compute.amazonaws.com' # DNS public du master
port = 5001
insert = 'INSERT INTO transactions VALUES ('
select = 'SELECT * FROM transactions WHERE serial = '


def main():
    """Main."""
    s = socket.socket()
    s.connect((host, port))

    with open('data_dump.csv', 'r') as f:
        lines = f.readlines()
        do_insert = True;
        for line in lines:
            print line
            member_id, date, country, gender, ip_address, amount, vip, product_id, card_type, serial, zone = line.split(",")
            if(insert):
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
