from Login import *
from click import *
from data import *

def test_end(driver):
    onWait_click(driver, "//*[@id='testSubmit']")
    a = driver.switch_to.alert
    a.accept()