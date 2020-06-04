from flask import json


def test_home_response_hello(client):
    """
    **Given** Vinicius is accessing the API,
    **When** he acess the route/endpoint '/',
    **Then** the API must return a object with key `['hello']`,
    **And** it's content must be `world by apps`
    """

    response = client.get('/')

    # Json func is used to return a dict to a var
    data = json.loads(response.data.decode('utf-8'))

    assert data['hello'] == 'world by apps'
