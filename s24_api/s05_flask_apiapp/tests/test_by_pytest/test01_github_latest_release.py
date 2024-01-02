import pytest
from src.flask_apiapp import app

@pytest.fixture
def apiapp():
  """Provides a test client for interacting with the Flask app."""
  with app.test_client() as apiapp:
    yield apiapp

def test(apiapp):
  res = apiapp.get('/github_latest_release')
  assert res.status_code == 200
  assert 'latest_release' in res.json
