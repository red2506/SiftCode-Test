from data import *
from click import onWait_click 

def deactivate(driver, xpath):
    
    """
    deactivate is used to click on the deactivate button.

    :driver: Instance of the chrome webdriver
    :xpath: XPATH of the deactivate button
    """ 

    try:
        onWait_click(driver, xpath)
    except:
        raise