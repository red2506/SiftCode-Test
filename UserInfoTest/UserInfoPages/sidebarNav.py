from click import *
from data import *
import time

def sidebar_navigation(driver):

    """
    sidebar_navigation is used to navigate to the profile option after extending the sidebar.

    :driver: Instance of the chrome webdriver
    """ 

    try:
        time.sleep(1)
        onWait_click(driver, "//*[@id='nav-mobile']/li[1]/a/i")
        onWait_click(driver, "//*[@id='slide-out']/li[6]/a")
        onWait_click(driver, "//*[@id='my_profile']/div/form/div/a/i")
    except:
        raise