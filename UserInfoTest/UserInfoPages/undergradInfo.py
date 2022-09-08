from data import onWait_data
from click import *

def undergraduate_info(driver):
    # College name
    onWait_click(driver,"//*[@id='candidate_info']/ul/li[5]/div[2]/div/div[1]/div[1]/div/input")
    onWait_click(driver,"//li[starts-with(@id, 'select-options-')]/span[(contains(., 'A.G.M. Rural Engineering College, Hubli'))]")

    # Stream
    onWait_click(driver,"//*[@id='candidate_info']/ul/li[5]/div[2]/div/div[2]/div[1]/div/input")
    onWait_click(driver,"//li[starts-with(@id, 'select-options-')]/span[(contains(., 'Information Science & Engineering'))]")

    # Scores
    onWait_data(driver,"//*[@id='be_avg']", "70")
    onWait_data(driver,"//*[@id='sem_1']", "70")
    onWait_data(driver,"//*[@id='sem_2']", "70")
    onWait_data(driver,"//*[@id='sem_3']", "70")
    onWait_data(driver,"//*[@id='sem_4']", "70")
    onWait_data(driver,"//*[@id='sem_5']", "70")
    onWait_data(driver,"//*[@id='sem_6']", "70")
    onWait_data(driver,"//*[@id='sem_7']", "70")
    onWait_data(driver,"//*[@id='sem_8']", "70")

    # Continue
    onWait_click(driver,"//*[@id='candidate_info']/ul/li[5]/div[2]/div/div[4]/div/button[2]")
