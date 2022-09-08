import logging
from logging.handlers import RotatingFileHandler
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *

def onWait_click(driver, xpath):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    fh = RotatingFileHandler('master.log', maxBytes=2000000, backupCount=10)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    
    try:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
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
    except UnexpectedTagNameException as exception:
        logger.error("Unexpected tag exception")
        raise 
    except InvalidCoordinatesException as exception:
        logger.error("Invalid coordinates exception")
        raise
    except ErrorInResponseException as exception:
        logger.error("Error in server side")
        raise
    except ImeNotAvailableException as exception:
        logger.error("IME support not available")
        raise