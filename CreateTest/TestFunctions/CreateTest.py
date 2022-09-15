from click import *
from data import *
import time

def create_test(driver):

    """
    create_test is used to create a test by fetching questionsalready existing in the Database.
    Here an Excel file is uploaded which contains questions with the tag 'GK' and difficulty 1 for the ease of testing.

    :driver: Instance of the chrome webdriver
    :xpath: XPATH of the activate test button
    """ 

    try:
        onWait_click(driver, "//*[@id='hometab']/div/ul/li[2]/a")
        onWait_data(driver, "//*[@id='main']/div/form/div[1]/div/div[1]/div[1]/div[1]/input","Some Test")
        onWait_data(driver, "//*[@id='main']/div/form/div[1]/div/div[1]/div[1]/div[2]/input","5" )
        onWait_data(driver,"//*[@id='main']/div/form/div[1]/div/div[2]/div/div/textarea", "Do It")
        onWait_data(driver,"//*[@id='main']/div/form/div[1]/div/div[4]/div[2]/div/table/tbody[2]/tr/td[1]/input", "2")
        onWait_click(driver, "//*[@ng-model='questionType.tag']/option[contains(text(), 'GK')]")  #must contain tag called GK
        onWait_click(driver, "//*[@id='main']/div/form/div[1]/div/div[4]/div[2]/div/table/tbody[2]/tr/td[3]/select/option[2]")   #must be difficulty 1
        time.sleep(5)
        onWait_click(driver, "//*[@id='main']/div/form/div[1]/div/div[4]/div[3]/div[2]/input")
        time.sleep(3)
        onWait_click(driver,"//*[@id='main']/div/form/div[2]/div/button")
    except:
        raise