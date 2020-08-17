from selenium.webdriver.common.by import By
class loginPage():
    
    textbox_username_id ="Email"
    testbox_password_id="Password"
    click_login_xpath="//input[@class='button-1 login-button']"
    click_logout_xpath="//a[contains(text(),'Logout')]"
    
    def __init__(self,driver):
        self.driver=driver
            
    def enterUserName(self,username):
        self.driver.find_element(By.ID,self.textbox_username_id).clear()
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)
        
    def enterPassword(self,password):
        self.driver.find_element(By.ID,self.testbox_password_id).clear()
        self.driver.find_element(By.ID,self.testbox_password_id).send_keys(password)
    
    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.click_login_xpath).click()
        
    def clickLogout(self):
        self. driver.find_element(By.XPATH,self.click_logout_xpath).click()
        
    