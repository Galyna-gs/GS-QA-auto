import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    
    assert user['login'] == 'defunkt'

@pytest.mark.api
def test_non_exist_user(github_api):
    r = github_api.get_user('butenko_sergii')
    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    # print(r)
    assert r['total_count'] == 57
    assert 'become-qa-auto' in r['items'][0]['name']
    
@pytest.mark.api
def test_cannot_be_fount(github_api):
    r = github_api.search_repo('gs_repo_non_exist')
    assert r['total_count'] == 0

@pytest.mark.api
def test_one_symbol_name(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0