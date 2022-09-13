from data import *
from click import *
from Login import *
from Logout import *
from CreateTest.TestFunctions.CreateTest import *
from CreateTest.TestFunctions.ActivateTest import *
from CreateTest.TestFunctions.CreateUser import *
from CreateTest.TestFunctions.ALogout import *

def test_creation(driver):

    """
    test_creation is the main function which runs all the sub-tasks for test creation.

    :driver: Instance of the chrome webdriver
    """

    # Setting up the logger for logging the data to the master.log file
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    fh = RotatingFileHandler('master.log', maxBytes=2000000, backupCount=10)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    
    try:
        login(driver, "tenekaw303@nicoimg.com", "1234")
        create_test(driver)
        activate_test(driver, "//*[contains(text(),'Some Test')]/parent::div/following-sibling::div[3]//*[@id='activate-test']")
        create_user(driver)
        admin_logout(driver, "/html/body/div[1]/div/div[1]/div[2]/header/button")
    except:
        logger.error("Test creation failed abruptly")
        raise
