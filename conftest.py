import pytest
from utils.client import Client

import logging


@pytest.fixture(scope='class', autouse=True)
def setup(request):
    logging.info('Initializing objects')
    request.cls.BASE_URL = 'https://lx8ssktxx9.execute-api.eu-west-1.amazonaws.com'
    request.cls.header = {'User-Agent': 'python-requests/2.31.0',
                          'Accept-Encoding': 'gzip, deflate',
                          'Accept': '*/*',
                          'Connection': 'keep-alive'
                          }
    request.cls.log = logging.getLogger()
    request.cls.clientUtil = Client(base_url=request.cls.BASE_URL, header=request.cls.header, log=request.cls.log)
    yield
    logging.info('Teardown steps can be written here')

