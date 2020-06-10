from os.path import dirname, isfile, join

import pytest
from dotenv import load_dotenv

# Set the path to .env file
_ENV_FILE = join(dirname(__file__), '../.env')

if isfile(_ENV_FILE):
    load_dotenv(dotenv_path=_ENV_FILE)


@pytest.fixture(scope='session')
def client():
    from apps import create_app
    # Instance flask in testing mode
    flask_app = create_app('testing')
    testing_client = flask_app.test_client()

    # Creates the context with config before the application
    context = flask_app.app_context()
    context.push()

    yield testing_client  # Test happens here

    context.pop()  # Remove the context after the tests


@pytest.fixture(scope='function')
def postgres(request, client):
    def fin():
        print('\n[teardown] disconnect from db')

    fin()
