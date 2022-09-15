from data import onWait_data
from click import *

def class12_info(driver):

    """
    class12_info is used to fill the user's class 12th details.

    :driver: Instance of the chrome webdriver
    """ 

    try:
        # Percentage
        onWait_data(driver, "//*[@id='class_xii']", "78")

        # Year
        onWait_data(driver, "//*[@id='class_xii_year']", "2018")

        # Continue
        onWait_click(driver, "//*[@id='candidate_info']/ul/li[4]/div[2]/div/div[4]/div/button[2]")
    except:
        raise