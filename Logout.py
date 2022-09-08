from click import *

def logout(driver):
    onWait_click(driver, "//*[@id='nav-mobile']/li[2]/a")