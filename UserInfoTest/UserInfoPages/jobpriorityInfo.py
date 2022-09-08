from data import *
from click import *

def jobPriority_info(driver):
    # Job Priority 
    onWait_click(driver,"//*[@id='candidate_info']/ul/li[6]/div[2]/div/div[2]/div[1]/div[1]/div/input")
    onWait_click(driver,"(//*[starts-with(@id, 'select-options-')]/span[(contains(., 'Networking'))])[1]")

    # Job Priority 2
    onWait_click(driver,"//*[@id='candidate_info']/ul/li[6]/div[2]/div/div[2]/div[1]/div[2]/div/input")
    onWait_click(driver,"(//*[starts-with(@id, 'select-options-')]/span[(contains(., 'Development'))])[2]")

    # Job Priority 3
    onWait_click(driver,"//*[@id='candidate_info']/ul/li[6]/div[2]/div/div[2]/div[2]/div[1]/div/input")
    onWait_click(driver,"(//*[starts-with(@id, 'select-options-')]/span[(contains(., 'Database'))])[3]")

    # # Job Priority 4
    onWait_click(driver,"//*[@id='candidate_info']/ul/li[6]/div[2]/div/div[2]/div[2]/div[2]/div/input")
    onWait_click(driver,"(//*[starts-with(@id, 'select-options-')]/span[(contains(., 'Security'))])[4]")

    # # Continue
    onWait_click(driver,"//*[@id='candidate_info']/ul/li[6]/div[2]/div/div[3]/div/button[2]")