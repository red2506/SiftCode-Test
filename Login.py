from click import *
from data import *

def login(driver):
    driver.get("http://localhost:9000/login")
    onWait_data(driver, "/html/body/div/div/div/div/div/div/form/div[1]/input", "tenekaw303@nicoimg.com")
    onWait_data(driver, "/html/body/div/div/div/div/div/div/form/div[2]/input", "1234")
    onWait_click(driver, "/html/body/div/div/div/div/div/div/form/button")
