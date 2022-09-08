from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import logging
from logging.handlers import RotatingFileHandler
from selenium.common.exceptions import *

def onWait_data(driver, xpath, data):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    fh = RotatingFileHandler('master.log', maxBytes=2000000, backupCount=10)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath))).clear()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath))).send_keys(data)
    except NoSuchElementException as exception:
        logger.error("Element not found and test failed")
        raise 
    except ElementNotInteractableException as exception:
        logger.error("Element not interactable")
        raise 
    except ElementNotSelectableException as exception:
        logger.error("Element not selectable")
        raise 
    except ElementNotVisibleException as exception:
        logger.error("Element not visible")
        raise 
    except TimeoutException as exception:
        logger.error("Timeout exception")
        raise 