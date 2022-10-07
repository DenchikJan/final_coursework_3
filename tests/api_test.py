import pytest

from main import app


def test_app():

    response = app.test_client().get('/api/posts')
    assert response.status_code == 200
    assert type(response.json) == list
    assert list(response.json[0].keys()) == ['content', 'likes_count', 'pic', 'pk', 'poster_avatar', 'poster_name', 'views_count']


def test_app_2():

    response = app.test_client().get('/api/posts/1')
    assert response.status_code == 200
    assert type(response.json) == dict
    assert list(response.json.keys()) == ['content', 'likes_count', 'pic', 'pk', 'poster_avatar', 'poster_name', 'views_count']




