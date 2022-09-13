from argparse import Action
from data import *
from click import *
import time

def uploadDocs_info(driver):

    """
    uploadDocs_info is used to upload the profile picture and the resume.

    :driver: Instance of the chrome webdriver
    """ 

    try:
        #Profile Pic
        onWait_click(driver, "//*[@id='candidate_info']/ul/li[7]/div[2]/div/div[1]/div[1]/a")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='profilePicture']"))).send_keys("C:/Users/Naveen/Desktop/Internship/FLASK/AutomationScripts/UserDocuments/images.jpg")
        
        #Resume
        time.sleep(1)
        onWait_click(driver, "//*[@id='candidate_info']/ul/li[7]/div[2]/div/div[1]/div[2]/div/a")
        onWait_data(driver, "//*[@id='resume']", "C:/Users/Naveen/Desktop/Internship/FLASK/AutomationScripts/UserDocuments/sample.pdf")
        onWait_click(driver, "//*[@id='upload-picture']")
        
        #submit
        time.sleep(8)
        onWait_click(driver, "//*[@id='submit_info']")
    except:
        raise