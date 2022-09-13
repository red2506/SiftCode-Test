from click import *

def admin_logout(driver, xpath):

    """
    admin_logout is used to click on the logout button.

    :driver: Instance of the chrome webdriver
    :xpath: XPATH of the logout button
    """ 

    try:
        onWait_click(driver, xpath)   
    except:
        raise