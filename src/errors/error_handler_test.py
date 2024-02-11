from src.errors.error_handler import handle_errors
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError

def test_handle_error_http_unprocessed_entity():
    error = HttpUnprocessableEntityError('Invalid input data')

    response = handle_errors(error)
    status_code = response.status_code
    errors = response.body['errors'][0]

    assert status_code == 422
    assert 'errors' in response.body
    assert 'title' in errors
    assert 'detail' in errors
