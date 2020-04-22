import logging

from splunk_handler import SplunkHandler

TOKEN='eyJraWQiOiJzcGx1bmsuc2VjcmV0IiwiYWxnIjoiSFM1MTIiLCJ2ZXIiOiJ2MiIsInR0eXAiOiJzdGF0aWMifQ.eyJpc3MiOiJhZG1pbiBmcm9tIHNwbHVuayIsInN1YiI6ImFkbWluIiwiYXVkIjoiY2hla2MiLCJpZHAiOiJTcGx1bmsiLCJqdGkiOiIzYjk4N2ZmMjk4NDU1NTc1NGY4NmFiMDIwYTg3ZGI1NmNlMGY0ZTllYzk0MzQxMTQwNmJiMjIxMzUxMWZhNWY4IiwiaWF0IjoxNTg3NTYxMTEyLCJleHAiOjAsIm5iciI6MTU4NzU2MTExMn0.HIsFjHtL2nf1Xgz3R746QyXQGJRv47J5f5urU4XExqIOv9lsAGxNXJDi04wBqCJjNthy-dAotNYh2yhdsrwK7g'

splunk = SplunkHandler(host='localhost',
                       port=8088,
                       token=TOKEN,
                       index='imon_msc',
                       verify=False)

logging.getLogger('').addHandler(splunk)


def send_test_message():
    logging.error('TESTMESSAGE from Python3 TestApp')
    print("testapplication for Splunk messages")


if __name__ == "__main__":
    send_test_message()
