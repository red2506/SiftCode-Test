from Login import *
from click import *
from data import *

def test_begin(driver):
    onWait_click(driver, "//*[@id='test1']/div/div/div/div[2]/button")
    onWait_click(driver, "//*[@id='proceed']")