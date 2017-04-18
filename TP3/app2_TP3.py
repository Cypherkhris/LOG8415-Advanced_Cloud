#!/usr/bin/python
"""Python module that receives TCP requests."""

import socket

host = '127.0.0.1'
port = 5001


def main():
    """Main."""
    s = socket.socket()
    s.bind(('', port))

    s.listen(1)  # Listen to one connection
    c, addr = s.accept()
    print 'connection from: ' + str(addr)

    while True:
        data = c.recv(2048)  # Max bytes
        if not data:
            break
        print 'from connected user: ' + str(data)
        data = str(data)

        # TO DO ...

        # Implement a function that parses received data

        # type, command = parse_data(data)

        # We need to detect INSERT or SELECT
        # In case of "INSERT", we hit Master node in MySQL Cluster
        # In case of "SELECT", we call the

        # if type == 'insert':
        #     hit_master(command)
        # else:
        #   my_pattern(command)
        #

    # c.close()


def parse_data(data):
    """Function that takes the data and parses it."""
    command = ''
    # TO DO ...
    # Implement a function that parses the data and detects type of command
    return type, command


def my_pattern():
    """Implement algorithm of the pattern here."""
    # Connect to MySQL Cluster
    # Hit the database based on the algorithm
    # TO DO ...


if __name__ == '__main__':
    main()
