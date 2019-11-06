import time
import logging
from threading import Thread

import pytest
from bottle import Bottle, run

TEST_SERVER = {
    'thread': None,
    'content': 'abc',
    'port': 12000,
}


def thread_server():
    print('Starting test server on 0.0.0.0:%d' % TEST_SERVER['port'])
    app = Bottle()

    @app.route('/')
    def page_home():
        return TEST_SERVER['content']
    
    run(app, host='0.0.0.0', port=TEST_SERVER['port'])


@pytest.fixture(scope='session')#, autouse=True)
def test_server():
    th = Thread(target=thread_server)
    th.daemon = True
    th.start()
    # Give it time to start
    time.sleep(0.5)
    TEST_SERVER['thread'] = th
