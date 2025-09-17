import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
import time

@pytest.mark.ui 
def test_incorrect_user_name():
    # Create object for managing browser
    driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
    )
    # Open the page
    driver.get("https://github.com/login")
    # find field to enter login
    login_elem = driver.find_element(By.ID, "login_field")
    # enter wrong login
    login_elem.send_keys("wrongemail@gmail.com")

    pass_elem = driver.find_element(By.ID, "password")
    pass_elem.send_keys("wrong password")

    btn_elem = driver.find_element(By.NAME, "commit")
    btn_elem.click()

    assert driver.title == "Sign in to GitHub · GitHub"
    # time.sleep(3)
    # close browser
    driver.close()

