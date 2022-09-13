from UserInfoTest.UserInfoPages.personalInfo import *
from UserInfoTest.UserInfoPages.contactInfo import *
from Login import *
from UserInfoTest.UserInfoPages.sidebarNav import *
from UserInfoTest.UserInfoPages.classTenInfo import *
from UserInfoTest.UserInfoPages.classTwelveInfo import *
from UserInfoTest.UserInfoPages.undergradInfo import *
from UserInfoTest.UserInfoPages.uploadDocuments import *
from UserInfoTest.UserInfoPages.jobpriorityInfo import *
from Logout import *
from pandas import ExcelFile
import time

def user_fill_info(driver):

    """
    user_fill_info is the main file that runs the automation tests for filling user's information.

    :driver: Instance of the chrome webdriver
    """ 

    # Storing the Excel sheet which contains user's credentials in a variable 
    xls = ExcelFile('User_credentials/Users.xlsx')
    data = xls.parse(xls.sheet_names[0])

    # Setting up the logger for logging the data to the master.log file
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    fh = RotatingFileHandler('master.log', maxBytes=2000000, backupCount=10)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    try:
        for x in range(0,len(data)):
            username = str(data['Email'][x])
            password = str(data['Password'][x])

            time.sleep(1)
            login(driver, username, password)
            time.sleep(1)
            sidebar_navigation(driver)
            time.sleep(1)
            personal_info(driver)
            time.sleep(1)
            contact_info(driver)
            time.sleep(1)
            class10_info(driver)
            time.sleep(1)
            class12_info(driver)
            time.sleep(1)
            undergraduate_info(driver)
            time.sleep(1)
            jobPriority_info(driver)
            time.sleep(1)
            uploadDocs_info(driver)
            time.sleep(1)
            logout(driver)
    except Exception as e:
        print(e)
        logger.error("User Info Test failed abruptly")
        raise
    