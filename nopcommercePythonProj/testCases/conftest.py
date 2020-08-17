import pytest
from selenium import webdriver
from utilities.ReadConfigFile import ReadConfigFile
 

    
     
@pytest.fixture()
def setup():

    browserType=ReadConfigFile.getBrowserType()
    if browserType=="IE" :
        driver = webdriver.Firefox(executable_path="C:/Users/kishorenm/eclipse-workspace/nopcommercePythonProj/Drivers/IE.exe")
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver
    elif browserType=="CHROME" :
        driver = webdriver.Firefox(executable_path="C:/Users/kishorenm/eclipse-workspace/nopcommercePythonProj/Drivers/chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver
    elif browserType=="MOZILA" :
        driver = webdriver.Firefox(executable_path="C:/Users/kishorenm/eclipse-workspace/nopcommercePythonProj/Drivers/geckodriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver
    else:
        driver = webdriver.Firefox(executable_path="C:/Users/kishorenm/eclipse-workspace/nopcommercePythonProj/Drivers/chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver
    
    
# ****************** Pytest HTML Report *********************

def pytest_configure(config):
    config._metadata['Project Name'] = 'Nop Commerce'
    config._metadata['Model Name'] = 'Cusumar'
    config._metadata['Tester'] = 'Nanda'