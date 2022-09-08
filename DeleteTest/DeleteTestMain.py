from data import *
from click import *
from Login import *
from DeleteTest.DeleteTestFunctions.deactivateTest import *
from DeleteTest.DeleteTestFunctions.deleteTest import *
from DeleteTest.DeleteTestFunctions.ALogout import *

def test_deletion(driver):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    fh = RotatingFileHandler('master.log', maxBytes=2000000, backupCount=10)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    try:
        login(driver, "tenekaw303@nicoimg.com", "1234")
        deactivate(driver)
        delete_test(driver)
        admin_logout(driver)
    except:
        logger.error("Test creation failed abruptly")
        raise