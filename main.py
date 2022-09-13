"""
    This is the main test file from which all different tests (Test Creation, Login-Logout test, User Info fill test,
    Test submission, Test Deletion, SignUp test) are executed.py

    Prerequisites:
    1) Selenium - pip install selenium
    2) Pandas - pip install pandas
    3) Openpyxl - pip install openpyxl
"""
from logging.handlers import RotatingFileHandler
import os
from selenium import webdriver
from LoginLogoutTest.Login_logout import login_logout
from UserInfoTest.userInfo import user_fill_info
from AssessmentSubmissionTest.testSubmission import test_submission
from SignupTest.signUp import sign_up
from CreateTest.AdminMain import test_creation
from DeleteTest.DeleteTestMain import test_deletion
import logging

# Adding the Chrome webdriver to the environment
os.environ['PATH'] += "C:/Users/Naveen/Desktop/Internship/FLASK/chromedriver_win32"

# Setting up the logger for logging the data to the master.log file
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
fh = RotatingFileHandler('master.log', maxBytes=2000000, backupCount=10, mode='w')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

driver = webdriver.Chrome()
driver.maximize_window()

# Test Creation
try:
    test_creation(driver)
    logger.info("Test creration passed successfully")
except:
    logger.info("Test creation failed")

# Login-Logout test
try:
    login_logout(driver)
    logger.info("Login-Logout Test passed successfully")
except:
    logger.info("Login-Logout Test failed")

# Filling User-Info test 
try:
    user_fill_info(driver)
    logger.info("User Info Test passed successfully")
except:
    logger.info("User Info Test failed")
    
# Test submission
try:
    test_submission(driver)
    logger.info("Assessment Submission Test passed successfully")
except:
    logger.info("Assessment Submission Test failed")

# Test deletion
try:
    test_deletion(driver)
    logger.info("Test deletion passed successfully")
except:
    logger.info("Test deletion failed")

# SignUp test
# try:
#     sign_up(driver)
#     logger.info("Sign Up Test passed successfully")
# except:
#     logger.info("Sign Up Test failed")

# Closing the browser
driver.quit()

