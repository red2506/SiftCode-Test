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

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
fh = RotatingFileHandler('master.log', maxBytes=2000000, backupCount=10, mode='w')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

os.environ['PATH'] += "C:/Users/Naveen/Desktop/Internship/FLASK/chromedriver_win32"
driver = webdriver.Chrome()
driver.maximize_window()

# try:
#     test_creation(driver)
#     logger.info("Test creration passed successfully")
# except:
#     logger.info("Test creation failed")

# try:
#     login_logout(driver)
#     logger.info("Login-Logout Test passed successfully")
# except:
#     logger.info("Login-Logout Test failed")

try:
    user_fill_info(driver)
    logger.info("User Info Test passed successfully")
except:
    logger.info("User Info Test failed")

# try:
#     test_submission(driver)
#     logger.info("Assessment Submission Test passed successfully")
# except:
#     logger.info("Assessment Submission Test failed")

# try:
#     test_deletion(driver)
#     logger.info("Test deletion passed successfully")
# except:
#     logger.info("Test deletion failed")

# try:
#     sign_up(driver)
#     logger.info("Sign Up Test passed successfully")
# except:
#     logger.info("Sign Up Test failed")

driver.quit()

