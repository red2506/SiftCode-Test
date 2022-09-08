from data import onWait_data
from click import *

def contact_info(driver):
    onWait_data(driver,"//*[@id='mobile_number']", "9878201084")
    onWait_data(driver,"//*[@id='contact_number']", "9878201084")

    # Address
    onWait_data(driver,"//*[@id='address']", "G1 Balaji Nivas, 1st Cross Road Pratibha Industrial area, Yellechenahalli Bangalore, 560078")

    # Continue
    onWait_click(driver,"//*[@id='candidate_info']/ul/li[2]/div[2]/div/div[3]/div/button[2]")
