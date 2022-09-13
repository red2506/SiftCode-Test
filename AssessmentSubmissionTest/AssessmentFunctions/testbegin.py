from Login import *
from click import *
from data import *

def test_begin(driver):

    """
    test_begin is is used to begin the test.

    :driver: Instance of the chrome webdriver
    """

    try:
        onWait_click(driver, "//*[@id='test1']/div/div/div/div[2]/button")
        onWait_click(driver, "//*[@id='proceed']")
    except:
        raise