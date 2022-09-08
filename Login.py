from click import *
from data import *

def login(driver, username, password):
    driver.get("http://localhost:9000/login")
    onWait_data(driver, "/html/body/div/div/div/div/div/div/form/div[1]/input", username)
    onWait_data(driver, "/html/body/div/div/div/div/div/div/form/div[2]/input", password)
    onWait_click(driver, "/html/body/div/div/div/div/div/div/form/button")
