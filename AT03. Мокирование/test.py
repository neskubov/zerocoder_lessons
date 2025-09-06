import pytest
from main import fetch_random_cat_image

def test_fetch_random_cat_image_status_ok(mocker):
     mock = mocker.patch('main.requests.get')
     mock.return_value.status_code = 200
     mock.return_value.json.return_value = [
                                            {"id":"aua",
                                             "url":"https://cdn2.thecatapi.com/images/aua.jpg",
                                             "width":640,
                                             "height":640}
                                            ]

     result = fetch_random_cat_image()
     assert result == [
            {"id":"aua",
             "url":"https://cdn2.thecatapi.com/images/aua.jpg",
             "width":640,
             "height":640}
            ]


def test_fetch_random_cat_image_status_error(mocker):
    mock = mocker.patch('main.requests.get')
    mock.return_value.status_code = 404
    result = fetch_random_cat_image()

    assert result is None



