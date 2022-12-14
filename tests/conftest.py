__author__ = 'miserylab'

import pytest
from dotenv import load_dotenv


@pytest.fixture(scope='session', autouse=True)
def env():
    load_dotenv()
