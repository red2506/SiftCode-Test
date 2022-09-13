from Login import *
from click import *
from data import *

def test_end(driver):

    """
    test_end is used to end the test.

    :driver: Instance of the chrome webdriver
    """

    try:
        onWait_click(driver, "//*[@id='testSubmit']")
        a = driver.switch_to.alert
        a.accept()
    except:
        raise