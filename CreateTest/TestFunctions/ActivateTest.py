from data import *
from click import onWait_click 
def activate_test(driver):
    #clicks on activate button
    onWait_click(driver,"//*[contains(text(),'Some Test')]/parent::div/following-sibling::div[3]//*[@id='activate-test']") 
    
    