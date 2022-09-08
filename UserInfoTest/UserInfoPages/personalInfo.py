from data import onWait_data
from click import *

def personal_info(driver):
    onWait_data(driver,"//*[@id='first_name']", "Calden")
    onWait_data(driver,"//*[@id='middle_name']", "Michael")
    onWait_data(driver,"//*[@id='last_name']", "DSouza")



    # Date of birth
    onWait_click(driver,"//*[@id='candidate_info']/ul/li[1]/div[2]/div/div[1]/div[2]/div/div/label")
    # Year
    onWait_click(driver,"//*[starts-with(@id, 'pika-title-')]/div/div[2]")
    onWait_click(driver,"//*[starts-with(@id, 'select-options-')]/span[text()='2006']")

    # Month
    onWait_click(driver,"//*[starts-with(@id, 'pika-title')]/div/div[1]/input")
    onWait_click(driver,"//*[starts-with(@id, 'select-options-')]/span[text()='February']")

    # Day
    onWait_click(driver,"//*[starts-with(@aria-labelledby, 'pika-title-')]/tbody/tr/td/button[.='10']")

    # Submitting the date of birth
    onWait_click(driver,"//*[starts-with(@id, 'modal-')]/div/div[2]/div[2]/div/button[2]")

    # Submitting the date of birth
    onWait_click(driver,"//*[starts-with(@id, 'modal-')]/div/div[2]/div[2]/div/button[2]")

    # Gender
    onWait_click(driver,"//*[@id='candidate_info']/ul/li[1]/div[2]/div/div[1]/div[3]/div/div/div/input")
    onWait_click(driver,"//*[starts-with(@id, 'select-options-')]/span[(contains(., 'Male'))]")

    # Continue
    onWait_click(driver,"//*[@id='candidate_info']/ul/li[1]/div[2]/div/div[2]/div/button")