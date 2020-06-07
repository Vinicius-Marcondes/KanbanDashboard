from flask import jsonify

from .messages import (  # MSG_NO_DATA; MSG_PASSWORD_DIDNT_MATCH,; MSG_RESOURCE_CREATED
    MSG_ALREADY_EXISTS,
    MSG_DOES_NOT_EXIST,
    MSG_EXCEPTION,
    MSG_INVALID_DATA,
    MSG_PERMISSION_DENIED
)


def resp_invalid_data(resource: str, errors: dict, msg: str = MSG_INVALID_DATA) -> dict:
    """
    Responses 422 Unprocessable Entity
    """

    if not isinstance(resource, str):
        raise ValueError("String expected, " + resource + " received")

    response = jsonify({
        'resource': resource,
        'message': msg,
        'errors': errors
    })

    response.status_code = 422

    return response


def resp_exception(resource: str, description: str = '', msg=MSG_EXCEPTION) -> dict:
    """
    Responses 500 Internal Server Error
    """

    if not isinstance(resource, str):
        raise ValueError("String expected, " + resource + " received")

    response = jsonify({
        'resource': resource,
        'message': msg,
        'description': description
    })

    response.status_code = 500

    return response


def resp_does_not_exist(resource: str, description: str) -> dict:
    """
    Responses 404 not found
    """

    if not isinstance(resource, str):
        raise ValueError("String expected, " + resource + " received")

    response = jsonify({
        'resource': resource,
        'message': MSG_DOES_NOT_EXIST.format(description),
        'status_code': 404
    })

    response.status_code = 404

    return response


def resp_already_exists(resource: str, description):
    """
    Responses 400 Bad Request
    """

    if not isinstance(resource, str):
        raise ValueError("String expected, " + resource + " received")

    resp = jsonify({
        'resource': resource,
        'message': MSG_ALREADY_EXISTS.format(description),
    })

    resp.status_code = 400

    return resp


def resp_ok(resource: str, message: str, data=None, **extras):
    """
    Responses 200
    """

    response = {
        'status': 200,
        'message': message,
        'resource': resource
    }

    if data:
        response['data'] = data

    response.update(extras)

    resp = jsonify(response)

    resp.status_code = 200

    return resp


def resp_not_allowed_user(resource: str, msg: str = MSG_PERMISSION_DENIED):
    if not isinstance(resource, str):
        raise ValueError("String expected, " + resource + " received")

    resp = jsonify({
        'status': 401,
        'resource': resource,
        'message': msg
    })

    resp.status_code = 401

    return resp
