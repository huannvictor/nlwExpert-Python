from unittest.mock import patch
from src.controllers.tag_creator_controller import TagCreatorController
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.tag_creator_view import TagCreatorView

@patch.object(TagCreatorController, 'create')
def test_validate_and_create(mock_create):
    http_request = HttpRequest( body={ 'product_code': 'image_path' } )

    mock_value = {
        'data': {
            'type': 'Tag Image', 
            'count': 1, 
            'path': 'image_path.png'
        }
    }
    mock_create.return_value = mock_value

    tag_creator_view = TagCreatorView()

    response = tag_creator_view.validate_and_create(http_request)
    status_code = response.status_code
    body = response.body

    assert isinstance(response, HttpResponse)

    assert status_code == 200

    assert 'data' in body
    assert 'type' in body['data']
    assert 'count' in body['data']
    assert 'path' in body['data']

    assert body['data']['type'] == "Tag Image"
    assert body['data']['count'] == 1
    assert body['data']['path'] == "image_path.png"
