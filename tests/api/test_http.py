import pytest
import requests

@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print(r.text)

@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/defunkt')
    body = r.json()
    headers = r.headers

    assert body['name'] == 'Chris Wanstrath'
    assert r.status_code == 200
    assert headers['server'] == 'github.com'

@pytest.mark.http
def test_status_code():
    r = requests.get('https://api.github.com/users/sergii_butenko')
    assert r.status_code == 404

    
