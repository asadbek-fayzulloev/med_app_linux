import requests
<<<<<<< HEAD
r = requests.get('http://192.168.43.196:8888/index.php/user/list?limit=20')
print(r.json())
=======
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager


class SourcePortAdapter(HTTPAdapter):
    """"Transport adapter" that allows us to set the source port."""
    def __init__(self, port, *args, **kwargs):
        self._source_port = port
        super(SourcePortAdapter, self).__init__(*args, **kwargs)

    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(
            num_pools=connections, maxsize=maxsize,
            block=block, source_address=('', self._source_port))

s = requests.Session()
s.mount('http://', SourcePortAdapter(8888))
s.get('192.168.43.196:8888/index.php/user/list?limit=20')
print(s.json())
>>>>>>> 247dfd9c1184a9428a39298166319530a7483b9a