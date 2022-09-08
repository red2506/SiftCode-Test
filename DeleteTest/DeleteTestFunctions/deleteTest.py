from click import *
from data import *

def delete_test(driver):
    onWait_click(driver,"//*[contains(text(),'Some Test')]/parent::div/following-sibling::div[3]//*[@id='delete-test']")


#//div[@class='col-md-3 col-sm-12']/following-sibling::div

#//*[@id="tests"]/div[725]/div[1]/p

#//*[contains(text(),'Some Test')]/parent::div/following-sibling::div[3]/input[@id="delete-test"]

#//*[title="50"]/parent::store

#//*[@id="activate-test"]