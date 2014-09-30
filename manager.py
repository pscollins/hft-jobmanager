

class AbstractNetworkConnection:
    def get_hosts(self):
        raise NotImplementedError


class GridNetworkConnection(AbstractNetworkConnection):
    pass

class RCCNetworkConnection(AbstractNetworkConnection):
    pass

class Host:
    def __init__(self, network_connection):
        self._net = network_connection

    def free_memory(self):
        pass

    def total_memory(self):
        pass

    def is_idle(self):
        pass

    def new_job(self, input_file):
        pass

class Job:
    def __init__(self, network_connection):
        self._net = network_connection
