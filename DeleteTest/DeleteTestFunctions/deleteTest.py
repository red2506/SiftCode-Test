from click import *
from data import *

def delete_test(driver, xpath):

    """
    delete_test is used to click on the delete button.

    :driver: Instance of the chrome webdriver
    :xpath: XPATH of the delete button
    """ 

    onWait_click(driver, xpath)