import time
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
    '有人批次': '//*[@id="datagrid-row-r4-2-2"]',
    '批次3': '//*[@id="datagrid-row-r4-2-2"]',
    '无人批次': '//*[@id="datagrid-row-r4-2-10"]',
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
    '体检类型下拉按钮': '//*[@id="_easyui_textbox_input19"]',
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
    '有信用代码': '//*[@id="_easyui_combobox_i8_10"]',
    '无信用代码': '//*[@id="_easyui_combobox_i8_11"]',
    '批次下拉选择按钮': '//*[@id="formSearch"]/table/tbody/tr[2]/td[4]/span[1]/span',
    '批次输入框': '//*[@id="_easyui_textbox_input21"]',
    '批次搜索按钮': '//*[@id="dlgGrIdList"]/div/div/div[1]/table/tbody/tr/td/span/span',
    '批次搜索结果': '//*[@id="datagrid-row-r4-2-11"]',
    '证件编号输入框': '//*[@id="_easyui_textbox_input2"]',
    '证件编号': '//*[@id="datagrid-row-r5-2-0"]/td[15]',
    '姓名输入框': '//*[@id="_easyui_textbox_input1"]',
    'youdi团队': '//*[@id="_easyui_combobox_i8_3"]',
    '单位:测试X': '//*[@id="_easyui_combobox_i8_3"]',
    '目标行输入框': '//*[@id="_easyui_textbox_input23"]',
    '目标行确认': '//*[@id="formSearch"]/table/tbody/tr[2]/td[12]/span/span',
    '签到': '//*[@id="formSearch"]/table/tbody/tr[1]/td[12]',
    '体检登记管理': '//*[@id="accMenu"]/div[1]/div[2]/ul/li[2]',
    '编号更改按钮': '//*[@id="formSearch"]/table/tbody/tr[2]/td[1]/span/span',
    '登记编号': '//*[@id="_easyui_combobox_i7_3"]',
    '编号输入框': '//*[@id="_easyui_textbox_input1"]',
    '体检登记管理搜索': '//*[@id="btnSearch"]',
    '取消签到': '//*[@id="btnCancelSign"]/span/span[1]',
    '确定取消签到': '#bodyLayout > div.panel.window.messager-panel.messager-window > div.dialog-button.messager-button > a:nth-child(1)',
    '关闭体检登记管理': '//*[@id="tabs"]/div[1]/div[3]/ul/li[2]/a[2]',
    '关闭体检签到': '//*[@id="tabs"]/div[1]/div[3]/ul/li[2]/a[2]',
    '勾选搜索结果': '//*[@id="datagrid-row-r5-2-1"]/td[1]/div/input',
    '页签栏': '//*[@id="tabs"]/div[1]/div[3]',

}


class SignIn(object):
    def __init__(self, business, product, browser):
        self.xpath_dict = business_xpath_dict
        self.driver = Sign(product, self.xpath_dict, browser).driver
        if business == '体检签到':
            self.pe_sign_in()

    def pe_sign_in(self):
        self.driver.click_ele('体检签到')
        self.driver.driver.switch_to.frame(0)
        assert '签到' in self.driver.text_ele('签到页面'), '进入签到失败'

    # 签到验证完成后取消签到
    def cancel_sign_in(self, number1=None, number2=None, business=None, batch_name=None):
        self.driver.driver.switch_to.default_content()
        try:
            self.driver.click_ele('关闭体检签到')
            self.driver.click_ele('体检登记-关闭确认', By.CSS_SELECTOR)
        except KeyError:
            pass
        self.driver.click_ele('体检登记管理')
        self.driver.driver.switch_to.frame(0)
        if business == 'sign_in':
            self.driver.continuous_clicks('体检登记管理-删除|体检登记管理-确认删除')
        elif business == 'batch_sign_in':
            self.driver.click_ele('预约团队下拉按钮')
            time.sleep(5)
            self.driver.input_ele('预约团队搜索框', batch_name)
            self.driver.continuous_clicks('体检登记管理-搜索|体检登记管理-删除|体检登记管理-确认删除')
        else:
            self.driver.continuous_clicks(
                '编号更改按钮|登记编号|编号输入框：{}|体检登记管理搜索|取消签到'.format(number1))
            self.driver.click_ele('确定取消签到', By.CSS_SELECTOR)
            if number2 is not None:
                self.driver.double_click('编号输入框')
                self.driver.set_empty('编号输入框')
                self.driver.continuous_clicks('编号输入框：{}|体检登记管理搜索|取消签到'.format(number2))
                self.driver.click_ele('确定取消签到', By.CSS_SELECTOR)

    def input_move_focus(self, locate_value, input_value):
        """
        输入内容，输入完成后点击照片，用来满足一些需要移开焦点的需求
        :param locate_value:
        :param input_value:
        :return:
        """
        self.driver.continuous_clicks('{}_{}|登记人员照片'.format(locate_value, input_value))

    # 类型检查
    def type_check(self, check_name, times):
        pe_type_list = ['常规体检', '出入境体检', '婚烟检查/婚姻检查', '健康证', '两痘筛查/两癌筛查', '学生体检',
                        '医乐/医保', '幼儿体检', '职业病体检', '健康检查', '医共体专用', '职工体检', '多图报告',
                        '驾照体检', '健康证类型/健康证类迅']
        healthy_type_list = ['Zmy测试用/zmy测试用', '餐饮', '餐饮行业', '服务生', '互联网行业', '家政服务', '教育行业',
                             '金矿']
        culture_type_list = ['文盲或半文盲', '其他', '大学专科和专科', '中专', '技工学校', '高中', '初中', '小学']
        marriage_type_list = ['未婚', '已婚', '再婚', '复婚', '丧', '离婚', '未知']
        if check_name == '体检类型':
            for i in range(int(times)):
                self.driver.continuous_clicks('体检登记-体检类型|体检登记-体检类型{}'.format(i))
                if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 11 or i == 14:
                    assert '扩展信息' in self.driver.screenshot('扩展信息')
                assert self.driver.screenshot('体检登记-体检类型') in pe_type_list[i]
            return True
        elif check_name == '健康类别':
            self.driver.continuous_clicks('体检登记-体检类型|体检登记-体检类型3')
            for i in range(int(times)):
                self.driver.continuous_clicks('体检登记-健康类别/css|体检登记-健康类别{}/css'.format(i))
                try:
                    self.driver.click_ele('忽略替换套餐', By.CSS_SELECTOR)
                except:
                    pass
                assert self.driver.screenshot('体检登记-健康类别', By.CSS_SELECTOR) in healthy_type_list[i]
                if i == 2:
                    self.driver.click_ele('健康工种')
                    assert '后厨' in self.driver.screenshot('健康工种1')
                    self.driver.continuous_clicks('健康工种|既往史输入框：一个健康的人')
                    assert '一个健康的人' in self.driver.screenshot('既往史输入框')
            return True
        elif check_name == '文化类别':
            self.driver.click_ele('文化类别下拉按钮')
            result = self.driver.screenshot('文化类别-全部类型')
            for i in range(int(times)):
                assert culture_type_list[i] in result
            self.driver.click_ele('文化类别-小学')
            assert '小学' in self.driver.screenshot('文化类别输入框')
            self.driver.set_empty('文化类别输入框')
            self.driver.continuous_clicks('文化类别输入框：高中|文化类别-高中')
            assert '高中' in self.driver.screenshot('文化类别输入框')
            return True
        elif check_name == '婚姻类别':
            assert '未知' in self.driver.screenshot('婚姻类别输入框')
            self.driver.click_ele('婚姻类别下拉按钮')
            result = self.driver.screenshot('婚姻类别-全部类型')
            for i in range(int(times)):
                assert marriage_type_list[i] in result
            self.driver.click_ele('婚姻类别-未婚')
            assert '未婚' in self.driver.screenshot('婚姻类别输入框')
            self.driver.set_empty('婚姻类别输入框')
            self.driver.continuous_clicks('婚姻类别输入框：已婚|婚姻类别-已婚')
            assert '已婚' in self.driver.screenshot('婚姻类别输入框')
            return True
        elif check_name == '科室检查-体检类型':
            for i in range(1, int(times) + 1):
                self.driver.continuous_clicks('科室检查-体检类型|科室检查-体检类型{}'.format(i))
                assert self.driver.screenshot('科室检查-体检类型') in pe_type_list[i - 1]
            return True
