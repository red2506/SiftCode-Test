from data import onWait_data
from click import *

def contact_info(driver):

    """
    contact_info is used to fill the users contact details.

    :driver: Instance of the chrome webdriver
    """ 

    try:
        # Contact Number
        onWait_data(driver,"//*[@id='mobile_number']", "9878201084")
        onWait_data(driver,"//*[@id='contact_number']", "9878201084")

        # Address
        onWait_data(driver,"//*[@id='address']", "Brigade Software Park, 27th Cross Rd, Banashankari Stage II, Bengaluru - 560070")

        # Continue
        onWait_click(driver,"//*[@id='candidate_info']/ul/li[2]/div[2]/div/div[3]/div/button[2]")
    except:
        raise
