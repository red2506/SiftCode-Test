import logging
from logging.handlers import RotatingFileHandler
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *



def onWait_click(driver, xpath):

    """
    onWait_click called whenever selenium is used to click an element.

    :driver: Instance of the chrome webdriver
    :xpath: XPATH of the element to be clicked
    """ 

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    fh = RotatingFileHandler('master.log', maxBytes=2000000, backupCount=10)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    
    try:
        driver.implicitly_wait(10)
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
    except ImeNotAvailableException as exception:
        logger.error("IME support not available")
        raise
    except ElementClickInterceptedException as exception:
        logger.error("Element click intercepted")
        raise
    except ImeActivationFailedException as exception:
        logger.error("IME engine has failed")
        raise
    except InsecureCertificateException as exception:
        logger.error("Expired or invalid TLS certificate")
        raise
    except InvalidArgumentException as exception:
        logger.error("Invalid arguments - arguments passed to the command are either invalid or malformed")
        raise
    except InvalidElementStateException as exception:
        logger.error("Invalid element state")
        raise
    except StaleElementReferenceException as exception:
        logger.error("Reference to the element is stale")
        raise
    

