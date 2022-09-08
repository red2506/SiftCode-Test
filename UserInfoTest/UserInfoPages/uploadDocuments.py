from data import *
from click import *
import time

def uploadDocs_info(driver):
    #profile Pic
    onWait_click(driver,"//*[@id='candidate_info']/ul/li[7]/div[2]/div/div[1]/div[1]/a")
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='profilePicture']"))).send_keys("C:/Users/Naveen/Downloads/img1.jpeg")
    onWait_click(driver,"//*[@id='profile_photo_close']")
    #Resume
    onWait_click(driver,"//*[@id='candidate_info']/ul/li[7]/div[2]/div/div[1]/div[2]/div/a")
    onWait_data(driver,"//*[@id='resume']", "C:/Users/Naveen/Downloads/blank.pdf")
    onWait_click(driver,"//*[@id='upload-picture']")
    
    #submit
    time.sleep(8)
    onWait_click(driver,"//*[@id='submit_info']")