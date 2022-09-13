from data import *
from click import onWait_click 
import time

def create_user(driver):

    """
    create_user is used to add the Excel file(Users.xlsx) containing user's email.

    :driver: Instance of the chrome webdriver
    """

    try:
        time.sleep(2)
        onWait_click(driver,"//*[contains(text(),'Some Test')]/parent::div/following-sibling::div[3]//*[@value='Add Users']")
        onWait_data(driver,"//*[contains(text(),'Some Test')]/ancestor::div[2]/following-sibling::div[1]//div/input[starts-with(@id, 'file-')]","C:/Users/Naveen/Desktop/Internship/FLASK/AutomationScripts/User_credentials/Users_add.xlsx")
        onWait_click(driver,"//*[contains(text(),'Some Test')]/ancestor::div[2]/following-sibling::div[1]//div/select[starts-with(@id, 'country-upload-model-')]/option[3]")
        onWait_click(driver, "//*[contains(text(),'Some Test')]/ancestor::div[2]/following-sibling::div[1]//div[@class='fileupload-buttonbar']/div/button[2]")
        time.sleep(5)
        a = driver.switch_to.alert
        a.accept()
        onWait_click(driver, "//*[contains(text(),'Some Test')]/ancestor::div[2]/following-sibling::div[1]//*[contains(text(),'Close')]")
    except:
        raise