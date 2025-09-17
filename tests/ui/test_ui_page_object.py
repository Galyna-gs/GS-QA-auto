from modules.UI.page_objects.sign_in_page import SignInPage
import pytest

@pytest.mark.ui 
def test_check_incorrect_user_name_page_object():
    # Create page object
    sign_in_page = SignInPage()
    # go to the page by URL
    sign_in_page.go_to()
    # try to sign in
    sign_in_page.try_login("wrongemail@gmail.com", "wrong password")
    
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    sign_in_page.close()


