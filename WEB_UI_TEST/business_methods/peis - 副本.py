from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from WEB_UI_TEST.public_methods.sign_in import Sign
business_xpath_dict = {
    '取消': '/html/body/div[10]/div[2]/b/a',
    '工号': '//*[@id="_easyui_textbox_input1"]',
    '口令': '//*[@id="_easyui_textbox_input6"]',
    '登录': '//*[@id="btnLogin"]',
    '提醒内容': '//*[@id="divBtnRemind"]/a',
    'peis标题': '//*[@id="spanMainTitle"]',
    '体检签到': '//*[@id="divHome"]/div/ul[1]/li[6]',
    '签到页面': '//*[@id="btnSign"]',
    '全部批次选项': '//*[@id="formSearch"]/table/tbody/tr[2]/td[4]/span[1]/span',
    '有人批次': '//*[@id="datagrid-row-r4-2-3"]',
    '批次3': '//*[@id="datagrid-row-r4-2-2"]',
    '无人批次': '//*[@id="datagrid-row-r4-2-8"]',
    '批次确定': '//*[@id="btnGrIdListSave"]',
    '搜索': '//*[@id="btnSearch"]',
    'iframe': '//*[@id="94"]',
    '搜索结果': '//*[@id="datagrid-row-r5-2-0"]',
    '登记编号1': '//*[@id="datagrid-row-r5-2-0"]/td[5]',
    '登记编号2': '//*[@id="datagrid-row-r5-2-1"]/td[5]',
    '提示': '/html',
    '登记结束日期': '//*[@id="formSearch"]/table/tbody/tr[1]/td[2]/span[2]/span',
    '结束日期向前一年': '//*[@id="bodyLayout"]/div[16]/div/div[1]/div/div[1]/div[3]',
    '日期中间日': '//*[@id="bodyLayout"]/div[16]/div/div[1]/div/div[2]/table/tbody/tr[3]/td[4]',
    '日期范围提示': '#bodyLayout > div.panel.window.messager-panel.messager-window',
    '体检类型下拉按钮': '//*[@id="formSearch"]/table/tbody/tr[1]/td[8]/span',
    '体检类型1': '//*[@id="_easyui_combobox_i7_1"]',
    '体检类型2': '//*[@id="_easyui_combobox_i7_2"]',
    '体检类型3': '//*[@id="_easyui_combobox_i7_3"]',
    '体检类型4': '//*[@id="_easyui_combobox_i7_4"]',
    '体检类型5': '//*[@id="_easyui_combobox_i7_5"]',
    '体检类型6': '//*[@id="_easyui_combobox_i7_6"]',
    '体检类型7': '//*[@id="_easyui_combobox_i7_7"]',
    '体检类型8': '//*[@id="_easyui_combobox_i7_8"]',
    '体检类型9': '//*[@id="_easyui_combobox_i7_9"]',
    '体检类型10': '//*[@id="_easyui_combobox_i7_10"]',
    '体检类型11': '//*[@id="_easyui_combobox_i7_11"]',
    '体检类型12': '//*[@id="_easyui_combobox_i7_12"]',
    '体检类型13': '//*[@id="_easyui_combobox_i7_13"]',
    '体检类型14': '//*[@id="_easyui_combobox_i7_14"]',
    '体检类型15': '//*[@id="_easyui_combobox_i7_15"]',
    '单位输入框': '//*[@id="_easyui_textbox_input20"]',
    '单位下拉选择按钮': '//*[@id="formSearch"]/table/tbody/tr[1]/td[4]/span/span',
    '有信用代码': '//*[@id="_easyui_combobox_i8_9"]',
    '无信用代码': '//*[@id="_easyui_combobox_i8_10"]',
    '批次下拉选择按钮': '//*[@id="formSearch"]/table/tbody/tr[2]/td[4]/span[1]/span',
    '批次输入框': '//*[@id="_easyui_textbox_input21"]',
    '批次搜索按钮': '//*[@id="dlgGrIdList"]/div/div/div[1]/table/tbody/tr/td/span/span',
    '批次搜索结果': '//*[@id="datagrid-row-r4-2-12"]',
    '证件编号输入框': '//*[@id="_easyui_textbox_input2"]',
    '证件编号': '//*[@id="datagrid-row-r5-2-0"]/td[15]',
    '姓名输入框': '//*[@id="_easyui_textbox_input1"]',
    'youdi团队': '//*[@id="_easyui_combobox_i8_3"]',
    '单位：测试X': '//*[@id="_easyui_combobox_i8_2"]',
    '目标行输入框': '//*[@id="_easyui_textbox_input23"]',
    '目标行确认': '//*[@id="formSearch"]/table/tbody/tr[2]/td[12]/span/span',
    '签到': '//*[@id="formSearch"]/table/tbody/tr[1]/td[12]',
    '体检登记管理': '//*[@id="accMenu"]/div[1]/div[2]/ul/li[2]',
    '编号更改按钮': '//*[@id="formSearch"]/table/tbody/tr[2]/td[1]/span/span',
    '登记编号': '//*[@id="_easyui_combobox_i6_3"]',
    '编号输入框': '//*[@id="_easyui_textbox_input1"]',
    '体检登记管理搜索': '//*[@id="btnSearch"]',
    '取消签到': '//*[@id="btnCancelSign"]/span/span[1]',
    '确定取消签到': '#bodyLayout > div.panel.window.messager-panel.messager-window > div.dialog-button.messager-button > a:nth-child(1)',
    '关闭体检登记管理': '//*[@id="tabs"]/div[1]/div[3]/ul/li[2]/a[2]',
    '关闭体检签到': '//*[@id="tabs"]/div[1]/div[3]/ul/li[2]/a[2]',
    '勾选搜索结果': '//*[@id="datagrid-row-r5-2-1"]/td[1]/div/input',
}


class Business(object):
    def __init__(self, business, product, browser):
        self.xpath_dict = business_xpath_dict
        self.driver = Sign(product, self.xpath_dict, browser).driver
        if business == 'pe_check_in':
            self.pe_check_in()

    def pe_check_in(self):
        self.driver.click_ele('体检签到')
        self.driver.driver.switch_to.frame(0)
        assert '签到' in self.driver.text_ele('签到页面'), '进入签到失败'

    def cancel_check_in(self, number1, number2=None):
        self.driver.driver.switch_to.default_content()
        try:
            self.driver.click_ele('关闭体检签到')
        except:
            pass
        self.driver.click_ele('体检登记管理')
        self.driver.driver.switch_to.frame(0)
        self.driver.continuous_clicks('编号更改按钮|登记编号|编号输入框-{}|体检登记管理搜索|取消签到'.format(number1))
        self.driver.click_ele('确定取消签到', By.CSS_SELECTOR)
        if number2 is not None:
            self.driver.double_click('编号输入框')
            self.driver.ele_location(locate_value='编号输入框').send_keys(Keys.BACKSPACE)
            self.driver.continuous_clicks('编号输入框-{}|体检登记管理搜索|取消签到'.format(number2))
            self.driver.click_ele('确定取消签到', By.CSS_SELECTOR)


