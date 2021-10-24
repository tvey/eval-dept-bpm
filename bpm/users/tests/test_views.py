import pytest

from bpm.users.views import example

pytestmark = pytest.mark.django_db


def test_example_view_returns_valid_response(rf):
    request = rf.get('/users')
    response = example(request)
    assert response.status_code == 200
    assert 'Hello' in response.content.decode()
