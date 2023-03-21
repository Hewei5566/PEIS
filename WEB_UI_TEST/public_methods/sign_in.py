from WEB_UI_TEST.public_methods.page_base import *


class Sign(object):
    def __init__(self, product, xpath_dict, browser):
        self.xpath_dict = xpath_dict
        self.driver = BaseMethods(browser, xpath_dict)
        if product == 'peis':
            self.peis()

    def peis(self):
        self.driver.open_url('http://101.132.163.3:7996')
        try:
            self.driver.click_ele('取消')
        except:
            pass
        self.driver.input_ele('工号', '999')
        self.driver.input_ele('口令', 'ly123.')
        self.driver.click_ele('登录')
        try:
            self.driver.click_ele('提醒内容')
        except:
            pass
        assert '健康管理' in self.driver.text_ele('peis标题'), '登录失败'


