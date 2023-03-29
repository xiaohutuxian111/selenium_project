"""
@FileName：HomePage.py
@Author：stone
@Time：2023/3/28 14:35
@Description：邮箱首页选择菜单
"""
from page.BasePage import BasePage


class HomePage(BasePage):
    """邮箱首页选择菜单"""
    # 配置文件元素读取
    homePage = BasePage.cf.getLocatorsOrAccount("HomePageElements", "homePage")
    mailList = BasePage.cf.getLocatorsOrAccount("HomePageElements", "mailList")
    applicationCenter = BasePage.cf.getLocatorsOrAccount("HomePageElements", "applicationCenter")
    inBox = BasePage.cf.getLocatorsOrAccount("HomePageElements", "inBox")


    # 首页菜单选项
    def selectMenu(self, Menu="mailList"):
        # 邮箱首页选择菜单
        if Menu == "mailList":
            self.click(*HomePage.mailList)
        elif Menu == "homePahe":
            self.click(*HomePage.homePage)
        elif Menu == "applicationCenter":
            self.click(*HomePage.applicationCenter)
        elif Menu == "inBox":
            self.click(*HomePage.inBox)
        else:
            raise ValueError(
                '''
                菜单选项错误
                homepage ->首页
                mailList -> 通讯录
                applicationCenter -> 应用中心
                inBox ->收件箱                
                '''
            )

if __name__ == '__main__':
    from selenium  import webdriver
    from page.LoginPage import LoginPage
    driver = webdriver.Firefox()
    login = LoginPage(driver)
    login.login("账号",'密码')

    home = HomePage(driver)
    home.selectMenu()
