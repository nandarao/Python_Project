from utilities.ReadConfigFile import ReadConfigFile
from pageObject.loginPage import loginPage
from utilities import readExcelFile
# from utilities.readExcelFile import readExcelFile

import time


class Test_002_DDL_login:

    url=ReadConfigFile.getApplicationURL()
    path=ReadConfigFile.getDataFilePath()
#     excelRead = readExcelFile()
#     cols = excelRead.getRowCount1("LoginPageData")
       
    def test_loginPageLoginTitle(self,setup):
        self.driver=setup
        self.driver.get(self.url)
        self.lp=loginPage(self.driver)
         
        self.cols = readExcelFile.getRowCout(self.path, "LoginPageData")
#         self.cols = readExcelFile.getRowCount1("LoginPageData")
        print(self.cols)

        lst_Status =[]
        for i in range(2,self.cols+1):
            self.user_id = readExcelFile.readData(self.path, "LoginPageData", i, 1)
            self.Password1 = readExcelFile.readData(self.path, "LoginPageData", i, 2)
            self.Expected = readExcelFile.readData(self.path, "LoginPageData", i, 3)
#             self.user_id = readExcelFile.readCellData("LoginPageData", i, 1)
#             self.Password1 = readExcelFile.readCellData("LoginPageData", i, 2)
#             self.Expected = readExcelFile.readCellData("LoginPageData", i, 3)
            self.lp.enterUserName(self.user_id)
            self.lp.enterPassword(self.Password1)
            self.lp.clickLogin()
            time.sleep(5)
            HomePageTile = self.driver.title
            if HomePageTile=="Dashboard / nopCommerce administration":
                if self.Expected=="Pass":
                    lst_Status.append("Pass")
                    self.driver.save_screenshot(".\\Screenshots\\"+"Pass_HomePage_Screenshot.png")
                    self.lp.clickLogout()
                    time.sleep(5)
#                     self.driver.close()
#                     self.driver.quit()
                elif self.Expected=="Fail":
                    lst_Status.append("Fail")
                    self.driver.save_screenshot(".\\Screenshots\\"+"Pass_HomePage_Screenshot.png")
                    self.lp.clickLogout()
                    time.sleep(5)
#                     self.driver.close()
#                     self.driver.quit()
                
            elif HomePageTile!="Dashboard / nopCommerce administration":
                if self.Expected=="Pass":
                    lst_Status.append("Fail")
                    self.driver.save_screenshot(".\\Screenshots\\"+"Pass_HomePage_Screenshot.png")
                    time.sleep(5)
                    
                elif self.Expected=="Fail":
                    lst_Status.append("Pass")
                    self.driver.save_screenshot(".\\Screenshots\\"+"Pass_HomePage_Screenshot.png")
                    time.sleep(5)
                    
        if "Fail" in lst_Status:
            self.driver.quit()
            assert False
        
        else:
            self.driver.quit()
            assert True
                