from utilities.ReadConfigFile import ReadConfigFile
from pageObject.loginPage import loginPage

class Test_001_login:

    url=ReadConfigFile.getApplicationURL()
    userID=ReadConfigFile.getApplicationUserID()
    password=ReadConfigFile.getApplicationPassword()
    filePath = ReadConfigFile.getDataFilePath()
    
    
    def test_loginPageTile(self,setup):
        
        self.driver = setup
        self.driver.get(self.url)
        loginTitle=self.driver.title
        if loginTitle=="Your store. Login":
            assert True
            self.driver.save_screenshot(".\\Screenshots\\"+"Pass_LoginPage_Screenshot.png")
            self.driver.close()
            self.driver.quit()
#             self.logger.info("***********login Page open Secussuflly********")
        else:
            assert False
#             self.logger.info("***********login Page not opend********")
            self.driver.save_screenshot(".\\Screenshots\\"+"Fail_LoginPage_Screenshot.png")
            self.driver.close()
            self.driver.quit()
            
    def test_loginPageLoginTitle(self,setup):
        

        
        self.driver=setup
        self.driver.get(self.url)
        self.lp=loginPage(self.driver)
        self.lp.enterUserName(self.userID)
        self.lp.enterPassword(self.password)
        self.lp.clickLogin()
        HomePageTile = self.driver.title
        if HomePageTile=="Dashboard / nopCommerce administration":
            self.driver.save_screenshot(".\\Screenshots\\"+"Pass_HomePage_Screenshot.png")
            self.lp.clickLogout()
            self.driver.close()
            self.driver.quit()
            assert True
             
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"Fail_HomePage_Screenshot.png")
            self.lp.clickLogout()
            self.driver.close()
            self.driver.quit()
            assert False
