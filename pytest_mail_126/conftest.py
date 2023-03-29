"""
@FileName：conftest.py
@Author：stone
@Time：2023/3/28 17:02
@Description：
"""
import pytest
from selenium import webdriver
from py._xmlgen import html

_driver = None

# 测试失败的时添加截图和测试用例描述(用例的注释信息)

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """当测试失败时添加截图和测试用例描述，展示在html的报告中"""
    pytest_html =item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report,'extra',[])

    if report.when  == 'call' or report.when == 'setup':
        xfail = hasattr(report,'wasxail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::","_")+".png"
            screen_img = _capture_screenshot()
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
        report.description = str(item.function.__doc__)
        report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1,html.th("Description"))
    cells.insert(2,html.th("Test_nodeid"))
    cells.pop(2)

@pytest.mark.optionalhook
def pytest_html_results_table_row(report,cells):
    cells.insert(1,html.td(report.description))
    cells.insert(2,html.td(report.nodeid))
    cells.pop(2)



def  _capture_screenshot():
    """截图保存为base64"""
    return _driver.get_screenshot_as_base64()


def driver():
    global _driver
    print("-------------------open browser--------------")
    _driver = webdriver.Firefox()

    yield  _driver

    print("-------------------close brower--------------")
    _driver.quit()




