from Login import login
from Logout import logout
from AssessmentSubmissionTest.AssessmentFunctions.testbegin import *
from AssessmentSubmissionTest.AssessmentFunctions.testend import test_end
from pandas import ExcelFile

xls = ExcelFile('User_credentials/Users.xlsx')
data = xls.parse(xls.sheet_names[0])

def test_submission(driver):
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
            login(driver, username, password)
            test_begin(driver)
            test_end(driver)
    except:
        logger.error("Test Submission failed abruptly")
        raise