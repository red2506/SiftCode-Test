from click import *
from data import *

def sidebar_navigation(driver):
    onWait_click(driver, "//*[@id='nav-mobile']/li[1]/a/i")
    onWait_click(driver, "//*[@id='slide-out']/li[6]/a")
    onWait_click(driver, "//*[@id='my_profile']/div/form/div/a/i")