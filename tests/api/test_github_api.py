import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    
    assert user['login'] == 'defunkt'

@pytest.mark.api
def test_non_exist_user(github_api):
    r = github_api.get_user('butenko_sergii')
    assert r['message'] == 'Not Found'
