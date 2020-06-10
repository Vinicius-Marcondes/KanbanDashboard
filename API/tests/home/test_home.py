# import json

# Client is the fixture created in conftest, it can be passed through param and
# used ins the scope of the funcion


def test_index_responde_200(client):
    response = client.get('/')

    # Check the response
    assert response.status_code == 200
