from Login import login
from Logout import logout
from AssessmentSubmissionTest.AssessmentFunctions.testbegin import *
from AssessmentSubmissionTest.AssessmentFunctions.testend import test_end

def test_submission(driver):
    driver.get("http://localhost:9000/login")
    login(driver)
    test_begin(driver)
    test_end(driver)