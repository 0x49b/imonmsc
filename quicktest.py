import logging

from splunkhandler import SplunkHandler

splunk = SplunkHandler(
    host='localhost',
    port=8088,
    token='147d3b46-e7c9-456a-ad0c-5a79b2f2ffea',
    index='main',
    hostname='localhost',
    source='testapp',
    sourcetype='json',
    verify=False,
    debug=True
)

logging.getLogger('').addHandler(splunk)
logging.warning('hello!')
