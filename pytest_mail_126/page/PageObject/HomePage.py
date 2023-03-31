"""
@FileName：HomePage.py
@Author：stone
@Time：2023/3/30 19:54
@Description：邮箱首页
"""
from page.BasePage import BasePage
from util.perseConFile import ParseConFile


class HomePage(BasePage):
    # 配置文件读取元素
    do_conf = ParseConFile()
    # 首页
    homePage = do_conf.getLocatorsOrAccount("HomePageElements", "homePage")
    # 通讯录
    mailList = do_conf.getLocatorsOrAccount("HomePageElements", "mailList")
    # 应用中心
    applicationCenter = do_conf.getLocatorsOrAccount("HomePageElements", "applicationCenter")
    # 收件箱
    inBox = do_conf.getLocatorsOrAccount("HomePageElements", "inBox")

    def select_menu(self, menu='mailList'):
        # 邮箱首页选择菜单
        if menu == "mailList":
            self.click_mail_list_menu()
        elif menu == "homePage":
            self.click_home_page_menu()
        elif menu == "applicationCenter":
            self.click_application_center_menu()
        elif menu == "inBox":
            self.click_in_box_menu()
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

    def click_home_page_menu(self):
        return self.click(*HomePage.homePage)

    def click_mail_list_menu(self):
        return self.click(*HomePage.mailList)

    def click_application_center_menu(self):
        return self.click(*HomePage.applicationCenter)

    def click_in_box_menu(self):
        return self.click(*HomePage.inBox)
