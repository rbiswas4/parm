

import socket
from contextlib import closing

def check_socket(host, port):
    """
    Parameters
    ----------
    host : strong

    port : integer

    Returns
    -------
    integer 0 if open

    Examples
    --------
    >>> check_socket('127.0.0.1', 8888)

    Notes
    -----
    Entirely copied from https://stackoverflow.com/questions/19196105/how-to-check-if-a-network-port-is-open-on-linux/19196218#19196218
    """
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        return sock.connect_ex((host, port))
