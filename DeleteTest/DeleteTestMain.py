from data import *
from click import *
from Login import *
from DeleteTest.DeleteTestFunctions.deactivateTest import *
from DeleteTest.DeleteTestFunctions.deleteTest import *
from DeleteTest.DeleteTestFunctions.ALogout import *

def test_deletion(driver):

    """
    test_deletion is the main file used to run the sub-tasks for test deletion.

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
        deactivate(driver, "//*[contains(text(),'Some Test')]/parent::div/following-sibling::div[3]//*[@id='deactivate-test']")
        delete_test(driver, "//*[contains(text(),'Some Test')]/parent::div/following-sibling::div[3]//*[@id='delete-test']")
        admin_logout(driver, "/html/body/div[1]/div/div[1]/div[2]/header/button")
    except:
        logger.error("Test deletion failed abruptly")
        raise