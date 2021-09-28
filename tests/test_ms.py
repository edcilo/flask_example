import pytest

from ms import app as ms_app


@pytest.fixture
def app():
    with ms_app.app_context():
        pass

    yield ms_app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
