from data import onWait_data
from click import *
import time

def personal_info(driver):

    """
    personal_info function is used to fill the personal info page.

    :driver: Instance of the chrome webdriver
    """ 

    try:
        # First, Middle and Last name
        onWait_data(driver,"//*[@id='first_name']", "Abc")
        onWait_data(driver,"//*[@id='middle_name']", "Def")
        onWait_data(driver,"//*[@id='last_name']", "Ghi")

        # Date of birth
        onWait_click(driver,"//*[@id='date_of_birth']")
        
        # Year
        time.sleep(1)
        onWait_click(driver,"//*[starts-with(@id, 'pika-title-')]/div/div[2]/input")
        onWait_click(driver,"//*[starts-with(@id, 'select-options-')]/span[text()='2008']")

        # Month
        onWait_click(driver,"//*[starts-with(@id, 'pika-title')]/div/div[1]/input")
        onWait_click(driver,"//*[starts-with(@id, 'select-options-')]/span[text()='February']")


        # Day
        onWait_click(driver,"//*[starts-with(@aria-labelledby, 'pika-title-')]/tbody/tr/td/button[.='11']")

        # Submitting the date of birth
        onWait_click(driver,"//*[starts-with(@id, 'modal-')]/div/div[2]/div[2]/div/button[2]")

        # Gender
        onWait_click(driver,"//*[@id='candidate_info']/ul/li[1]/div[2]/div/div[1]/div[3]/div/div/div/input")
        onWait_click(driver,"//*[starts-with(@id, 'select-options-')]/span[(contains(., 'Male'))]")

        # Continue
        onWait_click(driver,"//*[@id='candidate_info']/ul/li[1]/div[2]/div/div[2]/div/button")
    except:
        raise