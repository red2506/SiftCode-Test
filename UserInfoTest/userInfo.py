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

def user_fill_info(driver):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    fh = RotatingFileHandler('master.log', maxBytes=2000000, backupCount=10)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    try:
        login(driver)
        sidebar_navigation(driver)
        personal_info(driver)
        contact_info(driver)
        class10_info(driver)
        class12_info(driver)
        undergraduate_info(driver)
        jobPriority_info(driver)
        uploadDocs_info(driver)
        time.sleep(8)
        logout(driver)
    except:
        logger.error("User Info Test failed abruptly")
        raise
    