import time
import datetime
from dateutil.relativedelta import relativedelta
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
    '提示': '/html',
    '科室检查': '//*[@id="divHome"]/div/ul[2]/li[2]',
    '科室检查页面': '//*[@id="divMainCenter"]/div[1]',
    '科室检查-搜索': '//*[@id="btnSearch"]',
    '科室检查-搜索结果': '//*[@id="divPersonsList"]/div/div/div[2]/div[2]/div[2]/table/tbody',
    '科室检查-开始日期': '//*[@id="formSearch"]/div[1]/span[2]/span',
    '科室检查-开始日期向前一月': '//*[@id="bodyLayout"]/div[35]/div/div[1]/div/div[1]/div[1]',
    '科室检查-开始日期向前一年': '//*[@id="bodyLayout"]/div[35]/div/div[1]/div/div[1]/div[3]',
    '科室检查-开始具体日期': '//*[@id="bodyLayout"]/div[35]/div/div[1]/div/div[2]/table/tbody/tr[3]/td[4]',
    '科室检查-结束日期': '//*[@id="formSearch"]/div[2]/span/span',
    '科室检查-结束日期向前一月': '//*[@id="bodyLayout"]/div[36]/div/div[1]/div/div[1]/div[1]',
    '科室检查-结束日期向前一年': '//*[@id="bodyLayout"]/div[36]/div/div[1]/div/div[1]/div[3]',
    '科室检查-结束具体日期': '//*[@id="bodyLayout"]/div[36]/div/div[1]/div/div[2]/table/tbody/tr[3]/td[4]',
    '科室检查-体检类型': '//*[@id="_easyui_textbox_input12"]',
    '科室检查-体检类型1': '//*[@id="_easyui_combobox_i2_1"]',
    '科室检查-体检类型2': '//*[@id="_easyui_combobox_i2_2"]',
    '科室检查-体检类型3': '//*[@id="_easyui_combobox_i2_3"]',
    '科室检查-体检类型4': '//*[@id="_easyui_combobox_i2_4"]',
    '科室检查-体检类型5': '//*[@id="_easyui_combobox_i2_5"]',
    '科室检查-体检类型6': '//*[@id="_easyui_combobox_i2_6"]',
    '科室检查-体检类型7': '//*[@id="_easyui_combobox_i2_7"]',
    '科室检查-体检类型8': '//*[@id="_easyui_combobox_i2_8"]',
    '科室检查-体检类型9': '//*[@id="_easyui_combobox_i2_9"]',
    '科室检查-体检类型10': '//*[@id="_easyui_combobox_i2_10"]',
    '科室检查-体检类型11': '//*[@id="_easyui_combobox_i2_11"]',
    '科室检查-体检类型12': '//*[@id="_easyui_combobox_i2_12"]',
    '科室检查-体检类型13': '//*[@id="_easyui_combobox_i2_13"]',
    '科室检查-体检类型14': '//*[@id="_easyui_combobox_i2_14"]',
    '科室检查-体检类型15': '//*[@id="_easyui_combobox_i2_15"]',
    '高级搜索': '//*[@id="btnSearchR"]/div[2]/div[1]',
    '搜索类型下拉按钮': '//*[@id="btnSearch"]/span/span[3]',
    '搜索信息表': '//*[@id="formSearch"]',
    '散客批次': '#bodyLayout > div:nth-child(54) > div > div > div > div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table > tbody > tr:nth-child(3)',
    '团队批次下拉按钮': '//*[@id="formSearch"]/div[7]/span[2]/span/a[2]',
    '团队批次输入框': '//*[@id="_easyui_textbox_input26"]',
    '团队批次搜索结果': '#bodyLayout > div:nth-child(54) > div > div > div > div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table > tbody > tr:nth-child(1)',
    '团队批次搜索按钮': '//*[@id="bodyLayout"]/div[45]/div/div/div/div[1]/table/tbody/tr/td[1]/span/span',
    '科室检查-姓名输入框': '//*[@id="_easyui_textbox_input1"]',
    '科室检查-单位输入框': '//*[@id="_easyui_textbox_input41"]',
    '科室检查-住址输入框': '//*[@id="_easyui_textbox_input3"]',
    '科室检查-编号输入框': '//*[@id="_easyui_textbox_input2"]',
    '科室检查-搜索重置': '//*[@id="btnReset"]',
    '开始日期信息栏': '//*[@id="formSearch"]/div[1]',
    '一周体检人员': '//*[@id="btnSearchR"]/div[4]/div[1]',
    '当月体检人员': '//*[@id="btnSearchR"]/div[5]/div[1]',
    '科室检查-已检': '//*[@id="formSearch"]/div[17]/div/label[4]/input',
    '科室检查-未检': '//*[@id="formSearch"]/div[17]/div/label[3]/input',
    '': '//*[@id="divTarget"]/div/div/div[2]/div[2]/div[2]/table[1]',
    '科室检查-搜索结果2编号': '#divPersonsList > div > div > div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table > tbody > tr:nth-child(2) > td:nth-child(3)',
    '科室检查-搜索结果1编号': '#divPersonsList > div > div > div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table > tbody > tr:nth-child(1) > td:nth-child(3)',
    '检查信息表': '//*[@id="divTarget"]/div/div/div[2]/div[2]/div[2]',
    '体检人员列表-编号输入框': '//*[@id="_easyui_textbox_input4"]',
    '科室检查-体检人员列表-编号输入框': '//*[@id="_easyui_textbox_input4"]',
    '提示确定': '#bodyLayout > div.panel.window.messager-panel.messager-window > div.dialog-button.messager-button > a',
    '科室检查-提示确定': '#bodyLayout > div.panel.window.messager-panel.messager-window > div.dialog-button.messager-button > a',
    '科室检查-取消': '//*[@id="btnCancelEdit"]',
    '提示取消': '#bodyLayout > div.panel.window.messager-panel.messager-window > div.dialog-button.messager-button > a:nth-child(2)',
    '科室检查-搜索结果2身份证': '#divPersonsList > div > div > div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table > tbody > tr:nth-child(2) > td:nth-child(13)',
    '科室检查-搜索结果1身份证': '#divPersonsList > div > div > div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table > tbody > tr:nth-child(1) > td:nth-child(13)',
    '科室检查-记录': '//*[@id="btnEdit"]',
    '科室检查-指标框1': '//*[@id="datagrid-row-r1-2-0"]/td[2]',
    '科室检查-指标框2': '//*[@id="datagrid-row-r1-2-1"]/td[2]',
    '科室检查-指标框3': '//*[@id="datagrid-row-r1-2-2"]/td[2]',
    '科室检查-指标框4': '//*[@id="datagrid-row-r1-2-3"]/td[2]',
    '科室检查-指标框5': '//*[@id="datagrid-row-r1-2-4"]/td[2]',
    '科室检查-指标框6': '//*[@id="datagrid-row-r1-2-5"]/td[2]',
    '指标结果模板': '#divTargetResultTemplate > div.panel.layout-panel.layout-panel-center > div > div > div.panel.datagrid.easyui-fluid > div > div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table',
    '指标结果模板替换': '#divTargetResultTemplate > div.panel.layout-panel.layout-panel-center > div > div > div.panel.datagrid.easyui-fluid > div > div.datagrid-view > div.datagrid-view2 > div.datagrid-body > table > tbody > tr:nth-child(1) > td:nth-child(8)',
    '科室检查-保存': '//*[@id="btnSave"]',
    '检查医生信息1': '//*[@id="datagrid-row-r1-2-0"]/td[9]',
    '检查时间信息1': '//*[@id="datagrid-row-r1-2-0"]/td[10]',
    '科室检查-取消检查': '//*[@id="btnCancel"]/span/span[1]',
    '科室检查-结果输入框': '#datagrid-row-r1-2-0 > td.datagrid-row-selected > div > table > tbody > tr > td > span > input',
    '': '#datagrid-row-r1-2-0 > td.datagrid-row-selected > div > table > tbody > tr > td > span > input',
    '科室检查-默认结果': '//*[@id="btnDefaultResult"]/span/span[1]',
    '科室检查-项目信息表': '//*[@id="divCenter"]/div[2]',
    '科室检查-诊断信息': '//*[@id="tabs"]/div[2]/div[3]/div/div/div/div[2]/div[2]/div[2]/table/tbody',
    '标记信息栏': '//*[@id="datagrid-row-r1-2-1"]/td[8]',
    '科室检查-科室小结信息栏': '//*[@id="_easyui_textbox_input19"]',
    '科室检查-科室小结选项栏': '//*[@id="tabs"]/div[2]/div[1]/div/div/div[1]/div',
    '科室检查-诊断选项栏': '//*[@id="tabs"]/div[2]/div[3]/div/div/div/div[1]',
    '科室检查-诊断': '//*[@id="tabs"]/div[1]/div[3]/ul/li[3]',
    '科室检查-诊断页面': '#bodyLayout > div:nth-child(52)',
    '科室检查-诊断新增': '//*[@id="tabs"]/div[2]/div[3]/div/div/div/div[1]/table/tbody/tr/td[1]',
    '科室检查-诊断模板1': '//*[@id="datagrid-row-r11-2-0"]',
    '科室检查-诊断模板2': '//*[@id="datagrid-row-r13-2-1"]',
    '科室检查-诊断模板3': '//*[@id="datagrid-row-r15-2-2"]',
    '科室检查-诊断模板4': '//*[@id="datagrid-row-r17-2-3"]',
    '科室检查-诊断删除': '//*[@id="tabs"]/div[2]/div[3]/div/div/div/div[1]/table/tbody/tr/td[4]',
    '科室检查-诊断模板搜索框': '//*[@id="_easyui_textbox_input28"]',
    '科室检查-诊断模板默认展示数': '//*[@id="bodyLayout"]/div[43]/div/div/div/div[3]/table/tbody/tr/td[1]/select',
    '科室检查-诊断模板展示数2': '//*[@id="bodyLayout"]/div[43]/div/div/div/div[3]/table/tbody/tr/td[1]/select/option[2]',
    '科室检查-诊断模板展示数3': '//*[@id="bodyLayout"]/div[43]/div/div/div/div[3]/table/tbody/tr/td[1]/select/option[3]',
    '科室检查-诊断模板展示数4': '//*[@id="bodyLayout"]/div[43]/div/div/div/div[3]/table/tbody/tr/td[1]/select/option[4]',
    '科室检查-诊断模板展示数5': '//*[@id="bodyLayout"]/div[43]/div/div/div/div[3]/table/tbody/tr/td[1]/select/option[5]',
    '科室检查-诊断模板底部信息栏': '//*[@id="bodyLayout"]/div[43]/div/div/div/div[3]',
    '科室检查-诊断模板信息': '//*[@id="bodyLayout"]/div[43]/div/div/div/div[2]/div[2]/div[2]/table',
    '科室检查-诊断模板页数输入框': '//*[@id="bodyLayout"]/div[43]/div/div/div/div[3]/table/tbody/tr/td[7]/input',
    '科室检查-诊断模板下一页': '//*[@id="bodyLayout"]/div[43]/div/div/div/div[3]/table/tbody/tr/td[10]',
    '科室检查-诊断模板上一页': '//*[@id="bodyLayout"]/div[43]/div/div/div/div[3]/table/tbody/tr/td[4]',
    '科室检查-诊断模板尾页': '//*[@id="bodyLayout"]/div[43]/div/div/div/div[3]/table/tbody/tr/td[11]',
    '科室检查-诊断模板首页': '//*[@id="bodyLayout"]/div[43]/div/div/div/div[3]/table/tbody/tr/td[3]',
    '科室检查-诊断描述输入框': '#datagrid-row-r5-2-0 > td:nth-child(4) > div > table > tbody > tr > td > span > input',
    '科室检查-诊断描述1': '//*[@id="datagrid-row-r5-2-0"]/td[4]',
    '科室检查-诊断处理意见输入框': '#datagrid-row-r5-2-0 > td:nth-child(9) > div > table > tbody > tr > td > div',
    '科室检查-诊断处理意见1': '//*[@id="datagrid-row-r5-2-0"]/td[9]',
    '科室检查-诊断向上': '//*[@id="tabs"]/div[2]/div[3]/div/div/div/div[1]/table/tbody/tr/td[2]',
    '科室检查-诊断向下': '//*[@id="tabs"]/div[2]/div[3]/div/div/div/div[1]/table/tbody/tr/td[3]',
    '科室检查-生成诊断': '//*[@id="tabs"]/div[2]/div[3]/div/div/div/div[1]/table/tbody/tr/td[6]',
    '科室检查-科室下拉按钮': '//*[@id="regionDisplayAll"]/div/span[2]/span',
    '科室检查-科室2': '//*[@id="_easyui_combobox_i4_1"]',
    '科室检查-个人信息栏': '//*[@id="formPersonInfo"]',
    '科室检查-撤销': '//*[@id="tabs"]/div[2]/div[3]/div/div/div/div[1]/table/tbody/tr/td[5]',
    '科室检查-弃检确认': '//*[@id="dlgInput_btnSave"]',
    '科室检查-弃检取消': '//*[@id="dlgInput_btnCancel"]',
    '科室检查-项目4': '//*[@id="datagrid-row-r1-2-3"]',
    '科室检查-项目5': '//*[@id="datagrid-row-r1-2-4"]',
    '科室检查-弃检': '//*[@id="btnAbandInspec"]/span/span[1]',
    '日期范围提示': '#bodyLayout > div.panel.window.messager-panel.messager-window',
}


class DepartInspect(object):
    def __init__(self, business, product, browser):
        self.xpath_dict = business_xpath_dict
        self.driver = Sign(product, self.xpath_dict, browser).driver
        if business == '科室检查':
            self.pe_department_inspection()

    def pe_department_inspection(self):
        self.driver.click_ele('科室检查')
        self.driver.driver.switch_to.frame(0)
        assert '检查科室' in self.driver.text_ele('科室检查页面'), '进入签到失败'

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

    def continuous_input(self, input_box1, input_value1,
                         input_box2=None, input_value2=None,
                         input_box3=None, input_value3=None,
                         input_box4=None, input_value4=None,
                         input_box5=None, input_value5=None):
        self.driver.input_ele(input_box1, input_value1)
        if input_box2 is not None and input_value2 is not None:
            self.driver.input_ele(input_box2, input_value2)
        if input_box3 is not None and input_value3 is not None:
            self.driver.input_ele(input_box3, input_value3)
        if input_box4 is not None and input_value4 is not None:
            self.driver.input_ele(input_box4, input_value4)
        if input_box5 is not None and input_value5 is not None:
            self.driver.input_ele(input_box2, input_value2)

    def week_search(self):
        now_time = time.strftime("%Y-%m-%d", time.localtime())
        default_result = now_time in self.driver.text_recognition('开始日期信息栏')
        self.driver.continuous_clicks('搜索类型下拉按钮|一周体检人员|科室检查-搜索')
        week_ago = (datetime.datetime.now() - relativedelta(weeks=1)).strftime("%Y-%m-%d")
        change_result = week_ago in self.driver.text_recognition('开始日期信息栏')
        search_result = len(
            self.driver.text_ele('科室检查-搜索结果')) != 0 or '没有搜索到相关人员' in self.driver.text_ele(
            '提示')
        result_list = [default_result, change_result, search_result]
        return result_list

    def month_search(self):
        now_time = time.strftime("%Y-%m-%d", time.localtime())
        default_result = now_time in self.driver.text_recognition('开始日期信息栏')
        self.driver.continuous_clicks('搜索类型下拉按钮|当月体检人员|科室检查-搜索')
        this_month_start = datetime.datetime(datetime.date.today().year, datetime.date.today().month, 1)
        change_result = str(this_month_start).split(' ')[0] in self.driver.text_recognition('开始日期信息栏')
        search_result = len(
            self.driver.text_ele('科室检查-搜索结果')) != 0 or '没有搜索到相关人员' in self.driver.text_ele(
            '提示')
        result_list = [default_result, change_result, search_result]
        return result_list

    def get_target_data(self, locate_value, column_number, form_name=None):
        """
        获取目标数据
        :param form_name: 一张表格可能被划分，爬取部分数据，该参数不填，获取整个数据，填写整张表的class_name
        :param locate_value: 目标数据所在表
        :param column_number: 目标数据所在列
        :return:
        """
        if form_name is None:
            table = self.driver.driver.find_elements_by_tag_name('table')
        else:
            table = self.driver.driver.find_elements_by_class_name(form_name)
        target = self.driver.ele_location(locate_value=locate_value)
        data = []
        for rows in table:
            if rows == target:
                target_row = rows.find_elements(By.TAG_NAME, 'tr')
                for columns in target_row:
                    target_column = columns.find_elements(By.TAG_NAME, 'td')
                    text = target_column[int(column_number)].text
                    data.append(text)
        return data

    def check_state(self):
        self.driver.continuous_clicks('科室检查-开始日期|科室检查-开始日期向前一月|科室检查-开始具体日期|科室检查-搜索')
        self.driver.click_ele('科室检查-未检')
        not_checked_data = self.get_target_data('检查信息表', '1', 'datagrid-body')
        not_check_list = []
        for i in not_checked_data:
            if i == '':
                state = True
                not_check_list.append(state)
            else:
                state = False
                not_check_list.append(state)
        second_not_check_result = False not in not_check_list
        not_checked_result = self.driver.text_ele('科室检查-搜索结果')
        self.driver.click_ele('科室检查-已检')
        check_list = []
        checked_data = self.get_target_data('检查信息表', '1', 'datagrid-body')
        for i in checked_data:
            if i == '':
                state = True
                check_list.append(state)
            else:
                state = False
                check_list.append(state)
        second_check_result = False in check_list
        checked_result = self.driver.text_ele('科室检查-搜索结果')
        compare_result = not_checked_result != checked_result
        result_list = [second_not_check_result, second_check_result, compare_result]
        return result_list

    def save_check(self):
        self.driver.click_ele('科室检查-已检')

        save_result = '202105281305' in self.driver.text_ele('科室检查-搜索结果1编号', By.CSS_SELECTOR)
        result1 = len(self.driver.text_ele('检查医生信息1')) != 0
        result2 = len(self.driver.text_ele('检查时间信息1')) != 0
        self.driver.click_ele('科室检查-取消检查')
        self.driver.click_ele('提示确定', By.CSS_SELECTOR)
        result_list = [save_result, result1, result2]
        return result_list

    def checked_result_save(self, input_type, input_value=None, number=None, save=None):
        self.account_check()
        self.driver.continuous_clicks('科室检查-开始日期|科室检查-开始日期向前一月|科室检查-开始具体日期|科室检查-搜索|'
                                      '体检人员列表-编号输入框：202105281305')
        self.driver.ele_location(locate_value='体检人员列表-编号输入框').send_keys(Keys.ENTER)
        self.driver.click_ele('提示确定', By.CSS_SELECTOR)
        self.driver.click_ele('科室检查-指标框1')
        if input_type == '模板输入':
            self.driver.click_ele('指标结果模板替换', By.CSS_SELECTOR)
        elif input_type == '键盘输入':
            self.driver.input_ele('科室检查-结果输入框', input_value, By.CSS_SELECTOR)
        elif input_type == '默认结果':
            self.driver.click_ele('科室检查-默认结果')
        elif input_type == '先输入后默认':
            self.driver.input_ele('科室检查-结果输入框', input_value, By.CSS_SELECTOR)
            self.driver.click_ele('科室检查-默认结果')
            assert input_value in self.driver.text_recognition('科室检查-指标框1')
            assert '未见异常' in self.driver.text_recognition('科室检查-项目信息表')
        elif input_type == '先默认后修改':
            self.driver.click_ele('科室检查-默认结果')
            self.driver.click_ele('科室检查-指标框1')
            self.driver.input_ele('科室检查-结果输入框', input_value, By.CSS_SELECTOR)
            assert input_value in self.driver.text_recognition('科室检查-指标框1')
            assert '未见异常' in self.driver.text_recognition('科室检查-项目信息表')
        if number is not None:
            self.driver.click_ele('指标结果模板替换', By.CSS_SELECTOR)
            for i in range(2, int(number) + 1):
                self.driver.click_ele(f'科室检查-指标框{i}')
                self.driver.click_ele('指标结果模板替换', By.CSS_SELECTOR)
        self.driver.click_ele('科室检查-保存')
        if save is None:
            result_list = self.save_check()
            return result_list

    def add_diagnosis(self, number):
        """
        新增诊断
        :param number: 新增诊断条数
        :return:
        """
        for i in range(1, int(number) + 1):
            self.driver.continuous_clicks(f'科室检查-诊断新增|科室检查-诊断模板{i}')
        self.driver.click_ele('科室检查-指标框2')

    def delete_diagnosis(self, number):
        """
        删除诊断
        :param number: 删除诊断条数
        :return:
        """
        self.driver.continuous_clicks('体检人员列表-编号输入框：ENTER|科室检查-记录|提示确定/css|科室检查-诊断')
        for i in range(int(number)):
            self.driver.continuous_clicks('科室检查-诊断删除|提示确定/css')
        self.driver.continuous_clicks(
            '科室检查-保存|提示确定/css|体检人员列表-编号输入框：ENTER|科室检查-取消检查|提示确定/css')

    def enter_diagnosis_sheet(self, step1=None, step2=None, step3=None, step4=None,
                              step5=None, step6=None, step7=None, step8=None):
        self.account_check()
        self.driver.continuous_clicks('体检人员列表-编号输入框：202105281305|体检人员列表-编号输入框：ENTER|提示确定/css|'
                                      '科室检查-指标框2|指标结果模板替换/css|科室检查-诊断')
        if step1 is not None:
            self.driver.continuous_clicks(f'科室检查-{step1}')
        if step2 is not None:
            self.driver.continuous_clicks(f'科室检查-{step2}')
        if step3 is not None:
            self.driver.continuous_clicks(f'科室检查-{step3}')
        if step4 is not None:
            self.driver.continuous_clicks(f'科室检查-{step4}')
        if step5 is not None:
            self.driver.continuous_clicks(f'科室检查-{step5}')
        if step6 is not None:
            self.driver.continuous_clicks(f'科室检查-{step6}')
        if step7 is not None:
            self.driver.continuous_clicks(f'科室检查-{step7}')
        if step8 is not None:
            self.driver.continuous_clicks(f'科室检查-{step8}')

    def page_change(self):
        self.driver.click_ele('科室检查-诊断模板下一页')
        result1 = '第102' in self.driver.text_recognition('科室检查-诊断模板底部信息栏')
        self.driver.click_ele('科室检查-诊断模板上一页')
        result2 = '第101' in self.driver.text_recognition('科室检查-诊断模板底部信息栏')
        self.driver.click_ele('科室检查-诊断模板尾页')
        result3 = '第695' in self.driver.text_recognition('科室检查-诊断模板底部信息栏')
        self.driver.click_ele('科室检查-诊断模板首页')
        result4 = '显示1到20' in self.driver.text_recognition('科室检查-诊断模板底部信息栏')
        result_list = [result1, result2, result3, result4]
        return result_list

    def input_diagnostic_info(self, ele1, ele2, input_value, locate_type):
        self.driver.click_ele(f'科室检查-{ele1}')
        self.driver.set_empty(f'科室检查-{ele2}', locate_type=locate_type)
        self.driver.input_ele(f'科室检查-{ele2}', input_value, locate_type=locate_type)

    def abandon_check(self):
        """
        弃检校验业务
        :return:
        """
        self.checked_result_save('模板输入', number=3, save='保存')
        time.sleep(2)
        self.driver.continuous_clicks('体检人员列表-编号输入框：ENTER')
        flag = self.driver.exists_judge('提示确定', By.CSS_SELECTOR)
        if flag is True:
            self.driver.continuous_clicks('提示确定/css|科室检查-弃检')
        else:
            self.driver.click_ele('科室检查-弃检')
        # self.click_ele('科室检查-弃检')
        result1 = '请选择要弃检的项目或指标' in self.driver.text_ele('提示')
        self.driver.continuous_clicks('提示确定/css|科室检查-指标框1|科室检查-弃检')
        result2 = '已有结果，不允许弃检' in self.driver.text_ele('提示')
        self.driver.continuous_clicks('提示确定/css|科室检查-指标框4|科室检查-弃检')
        result3 = self.driver.exists_judge('科室检查-弃检确认')
        self.driver.click_ele('科室检查-弃检取消')
        result4 = '弃检' not in self.driver.text_ele('科室检查-项目4')
        self.driver.continuous_clicks('科室检查-指标框5|科室检查-弃检|科室检查-弃检确认')
        result5 = '弃检' in self.driver.text_ele('科室检查-项目5')
        result_list = [result1, result2, result3, result4, result5]
        self.driver.continuous_clicks('科室检查-取消检查|提示确定/css')
        return result_list

    def account_check(self):
        self.driver.continuous_clicks('体检人员列表-编号输入框：202105281305|体检人员列表-编号输入框：ENTER')
        check_result = self.driver.exists_judge('提示确定', By.CSS_SELECTOR)
        if check_result is True:
            self.driver.continuous_clicks('提示确定/css|科室检查-取消|提示确定/css')
        else:
            self.driver.click_ele('科室检查-记录')
            flag = self.driver.exists_judge('提示确定', By.CSS_SELECTOR)
            if flag is True:
                self.driver.continuous_clicks('提示确定/css|科室检查-诊断')
            else:
                self.driver.click_ele('科室检查-诊断')
            for i in range(3):
                if len(self.driver.text_ele('科室检查-诊断信息')) > 5:
                    self.driver.continuous_clicks('科室检查-诊断删除|提示确定/css')
                else:
                    break
            self.driver.continuous_clicks('科室检查-保存|提示确定/css|体检人员列表-编号输入框：ENTER|科室检查-取消检查|提示确定/css')
        self.driver.set_empty('体检人员列表-编号输入框')
