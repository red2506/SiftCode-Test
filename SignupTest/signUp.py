from data import *
from click import *
from pandas import ExcelFile

xls = ExcelFile('User_credentials/Users.xlsx')
data = xls.parse(xls.sheet_names[0])

def sign_up(driver):
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
            driver.get("http://localhost:9000/signup")
            onWait_data(driver, "//*[@id='Form']/input[2]", username)
            onWait_data(driver, "//*[@id='Form']/input[3]", password)
            onWait_click(driver, "//*[@id='Form']/button")
    except:
        logger.error("SignUp failed abruptly")
        raise