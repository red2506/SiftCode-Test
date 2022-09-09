from data import onWait_data
from click import *

def class10_info(driver):
    # Percentage
    driver.implicitly_wait(10)
    onWait_data(driver,"//*[@id='class_x']", "74")
    driver.implicitly_wait(10)
    onWait_data(driver,"//*[@id='class_x_year']", "2015")

    # Continue
    onWait_click(driver,"//*[@id='candidate_info']/ul/li[3]/div[2]/div/div[3]/div/button[2]")