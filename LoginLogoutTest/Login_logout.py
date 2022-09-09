from Login import *
from Logout import *
from pandas import ExcelFile

xls = ExcelFile('User_credentials/Users.xlsx')
data = xls.parse(xls.sheet_names[0])

def login_logout(driver):
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
            print(username)
            login(driver, username, password)
            logout(driver)
    except:
        logger.error("Login-Logout failed abruptly")
        raise
