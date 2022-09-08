from data import *
from click import *

def sign_up(driver):
    driver.get("http://localhost:9000/signup")
    onWait_data(driver, "//*[@id='Form']/input[2]","abc123@gmail.com")
    onWait_data(driver, "//*[@id='Form']/input[3]","1234")
    onWait_click(driver, "//*[@id='Form']/button")