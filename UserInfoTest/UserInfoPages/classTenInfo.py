from data import onWait_data
from click import *

def class10_info(driver):

    """
    class10_info is used to fill the user's class 10th details.

    :driver: Instance of the chrome webdriver
    """ 

    try:
        # Percentage
        onWait_data(driver,"//*[@id='class_x']", "80")

        # Year
        onWait_data(driver,"//*[@id='class_x_year']", "2015")

        # Continue
        onWait_click(driver,"//*[@id='candidate_info']/ul/li[3]/div[2]/div/div[3]/div/button[2]")
    except:
        raise