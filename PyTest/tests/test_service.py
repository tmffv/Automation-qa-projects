import pytest
import requests

import source.service as service
import unittest.mock as mock


@mock.patch("source.service.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "Mocked Alice"
    user_name = service.get_user_from_db(1)

    assert user_name == "Mocked Alice"


"""
replace requests.get in the source.service module with a mock object.
When the test function test_get_users() is called, it will not actually make a real HTTP request 
but will use a mocked version of requests.get.

test_get_users - defines the test function.
mock_het - is the mock object representing the requests.get function.

mock_response - creates a mock object (mock_response) that will simulate the response from requests.get

mock_get.return_value - sets the return value of the mock requests.get (i.e., mock_get) to the mock response (mock_response).
"""
@mock.patch("source.service.requests.get")
def test_get_users(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "John Doe"}
    # Set the mock response to be returned by requests.get
    mock_get.return_value = mock_response
    # Call the function you're testing
    data = service.get_users()
    # Assert that the returned data matches the mock data
    assert data == {"id": 1, "name": "John Doe"}


"""
with - this is a pytest context manager that asserts that a specific exception (requests.HTTPError) 
is raised during the execution of the code inside the with block
"""
@mock.patch("source.service.requests.get")
def test_get_users_error(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_get.return_value = mock_response
    # expects an exception (requests.HTTPError) to be raised inside the with block
    with pytest.raises(requests.HTTPError):
        service.get_users()



