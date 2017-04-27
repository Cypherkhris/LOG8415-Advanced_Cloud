# From : https://pythonadventures.wordpress.com/2012/12/27/measuring-ping-latency-of-a-server/

import shlex
from subprocess import Popen, PIPE, STDOUT

def get_command_output(cmd, stderr=STDOUT):
    """
    Execute a simple external command and get its output
    """
    args = shlex.split(cmd)
    return Popen(args, stdout=PIPE, stderr=stderr).communicate()[0]

def get_ping_time(host, tryCount=3):
    host = host.split(':')[0]
    cmd = 'fping {host} -C {tryCount} -q'.format(host=host, tryCount=tryCount)
    res = [float(x) for x in get_command_output(cmd).strip().split(':')[-1].split() if x != '-']
    if len(res) > 0:
        return sum(res)/len(res)
    else:
        return 9999999