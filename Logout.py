from click import *

def logout(driver):

    """
    logout is used to logout from the account.

    :driver: Instance of the chrome webdriver
    """

    try:
        onWait_click(driver, "//*[@id='nav-mobile']/li[2]/a")
    except:
        raise