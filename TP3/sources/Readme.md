## Gatekeeper or proxy?

We have 2 main configuration:

* client -> Gatekeeper -> proxy
* client -> proxy

Is is possible to switch between the 2 in cluster.config and change the
target of [Client]


## Proxy mode

There is 3 choices for the proxy:

* direct: Use master directly
* random: Use a random slave
* balancing: Use the slave with lowest ping time


## Start the job

0. Install dependencies: sudo ./install.sh
1. Start proxy: python proxy.py
(on AWS instance : /usr/bin/python2.7 ./proxy.py)
2. Start gatekeeper (optional): python gatekeeper.py
(on AWS instance : /usr/bin/python2.7 ./gatekeeper.py)
3. Start client: python client.py
4. To stop: kill client to avoid not closing port on listener
