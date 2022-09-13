from data import *
from click import onWait_click


def activate_test(driver, xpath):

    """
    activate_test is used to click on the activate test button.

    :driver: Instance of the chrome webdriver
    :xpath: XPATH of the activate test button
    """

    try:
        onWait_click(driver, xpath)
    except:
        raise 
    
    