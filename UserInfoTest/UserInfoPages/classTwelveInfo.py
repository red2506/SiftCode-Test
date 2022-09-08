from data import onWait_data
from click import *

def class12_info(driver):
    onWait_data(driver, "//*[@id='class_xii']", "57")
    driver.implicitly_wait(10)
    onWait_data(driver, "//*[@id='class_xii_year']", "2018")

    # Continue
    onWait_click(driver, "//*[@id='candidate_info']/ul/li[4]/div[2]/div/div[4]/div/button[2]")