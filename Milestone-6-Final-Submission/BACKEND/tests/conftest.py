import pytest
from tests import app


@pytest.fixture
def client():
    return app.test_client()