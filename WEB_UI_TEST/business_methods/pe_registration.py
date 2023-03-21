from WEB_UI_TEST.business_methods.pe_sign_in import *
business_xpath_dict = {
    '取消': '/html/body/div[10]/div[2]/b/a',
    '工号': '//*[@id="_easyui_textbox_input1"]',
    '口令': '//*[@id="_easyui_textbox_input6"]',
    '登录': '//*[@id="btnLogin"]',
    '提醒内容': '//*[@id="divBtnRemind"]/a',
    'peis标题': '//*[@id="spanMainTitle"]',
    '提示': '/html',
    '体检登记': '//*[@id="divHome"]/div/ul[1]/li[3]',
    '体检登记页面': '//*[@id="btnReset"]',
    'HIS提示确定': '#bodyLayout > div.panel.window.messager-panel.messager-window > div.dialog-button.messager-button > a',
    '证件输入框': '//*[@id="_easyui_textbox_input95"]',
    '登记人员照片': '//*[@id="imgPhoto"]',
    '体检登记-体检类型': '//*[@id="_easyui_textbox_input144"]',
    '体检登记-体检类型0': '//*[@id="_easyui_combobox_i29_0"]',  # 常规体检
    '体检登记-体检类型1': '//*[@id="_easyui_combobox_i29_1"]',  # 出入境体检
    '体检登记-体检类型2': '//*[@id="_easyui_combobox_i29_2"]',  # 婚姻检查
    '体检登记-体检类型3': '//*[@id="_easyui_combobox_i29_3"]',  # 健康证
    '体检登记-体检类型4': '//*[@id="_easyui_combobox_i29_4"]',  # 两癌筛查
    '体检登记-体检类型5': '//*[@id="_easyui_combobox_i29_5"]',  # 学生体检
    '体检登记-体检类型6': '//*[@id="_easyui_combobox_i29_6"]',  # 医保
    '体检登记-体检类型7': '//*[@id="_easyui_combobox_i29_7"]',  # 幼儿体检
    '体检登记-体检类型8': '//*[@id="_easyui_combobox_i29_8"]',  # 职业病体检
    '体检登记-体检类型9': '//*[@id="_easyui_combobox_i29_9"]',  # 健康检查
    '体检登记-体检类型10': '//*[@id="_easyui_combobox_i29_10"]',  # 医共体专用
    '体检登记-体检类型11': '//*[@id="_easyui_combobox_i29_11"]',  # 职工体检
    '体检登记-体检类型12': '//*[@id="_easyui_combobox_i29_12"]',  # 多图报告
    '体检登记-体检类型13': '//*[@id="_easyui_combobox_i29_13"]',  # 驾照体检
    '体检登记-体检类型14': '//*[@id="_easyui_combobox_i29_14"]',  # 健康证类型
    '体检登记管理': '//*[@id="accMenu"]/div[1]/div[2]/ul/li[2]',
    '扩展信息': '//*[@id="divExtInfo"]', '#bodyLayout > div:nth-child('
                                         '切换导航栏': '//*[@id="imgMainTitle"]',
    '体检登记-健康类别0': '#bodyLayout > div:nth-child(83) > div:nth-child(1) > div:nth-child(1)',
    '体检登记-健康类别': '#tableExtInfo > tbody > tr:nth-child(13) > td:nth-child(2) > span',
    '体检登记-健康类别1': '#bodyLayout > div:nth-child(83) > div:nth-child(1) > div:nth-child(2)',
    '体检登记-健康类别2': '#bodyLayout > div:nth-child(83) > div:nth-child(1) > div:nth-child(3)',
    '体检登记-健康类别3': '#bodyLayout > div:nth-child(83) > div:nth-child(1) > div:nth-child(4)',
    '体检登记-健康类别4': '#bodyLayout > div:nth-child(83) > div:nth-child(1) > div:nth-child(5)',
    '体检登记-健康类别5': '#bodyLayout > div:nth-child(83) > div:nth-child(1) > div:nth-child(6)',
    '体检登记-健康类别6': '#bodyLayout > div:nth-child(83) > div:nth-child(1) > div:nth-child(7)',
    '体检登记-健康类别7': '#bodyLayout > div:nth-child(83) > div:nth-child(1) > div:nth-child(8)',
    '忽略替换套餐': '#bodyLayout > div.panel.window.messager-panel.messager-window > div.panel-header.panel-header-noborder.window-header > div.panel-tool',
    '健康工种': '//*[@id="_easyui_textbox_input135"]',
    '健康工种1': '//*[@id="bodyLayout"]/div[64]',
    '既往史输入框': '//*[@id="_easyui_textbox_input41"]',
    '文化类别下拉按钮': '//*[@id="divBaseInfo1"]/div[2]/div/table/tbody/tr[3]/td[3]/span[1]/span/a',
    '文化类别-全部类型': '//*[@id="bodyLayout"]/div[27]',
    '文化类别-小学': '//*[@id="_easyui_combobox_i5_7"]',
    '文化类别输入框': '//*[@id="_easyui_textbox_input79"]',
    '文化类别-高中': '//*[@id="_easyui_combobox_i5_5"]',
    '出生日期输入框': '//*[@id="_easyui_textbox_input102"]',
    '年龄': '//*[@id="_easyui_textbox_input96"]',
    '出生日期日历': '//*[@id="divBaseInfo1"]/div[2]/div/table/tbody/tr[2]/td[5]/span/span/a',
    '日历前一年': '//*[@id="bodyLayout"]/div[47]/div/div[1]/div/div[1]/div[3]',
    '日历前一月': '//*[@id="bodyLayout"]/div[47]/div/div[1]/div/div[1]/div[1]',
    '日历具体日期': '//*[@id="bodyLayout"]/div[47]/div/div[1]/div/div[2]/table/tbody/tr[3]/td[4]',
    '年龄输入框': '//*[@id="_easyui_textbox_input96"]',
    '体检登记姓名输入框': '//*[@id="_easyui_textbox_input4"]',
    '姓名行': '//*[@id="divBaseInfo1"]/div[2]/div/table/tbody/tr[2]',
    '性别切换': '//*[@id="_easyui_textbox_input137"]',
    '性别女': '//*[@id="_easyui_combobox_i25_1"]',
    '年龄输入提示': '//*[@id="divPeisCalendar"]',
    '电话输入框': '//*[@id="_easyui_textbox_input140"]',
    '婚姻类别输入框': '//*[@id="_easyui_textbox_input139"]',
    '婚姻类别下拉按钮': '//*[@id="divBaseInfo1"]/div[2]/div/table/tbody/tr[3]/td[3]/span[3]/span/a',
    '婚姻类别-全部类型': '//*[@id="bodyLayout"]/div[25]',
    '婚姻类别-未婚': '//*[@id="_easyui_combobox_i27_0"]',
    '婚姻类别-已婚': '//*[@id="_easyui_combobox_i27_1"]',
    '省份输入框': '//*[@id="_easyui_textbox_input104"]',
    '城市输入框': '//*[@id="_easyui_textbox_input105"]',
    '区域输入框': '//*[@id="_easyui_textbox_input106"]',
    '街道输入框': '//*[@id="_easyui_textbox_input107"]',
    '村委输入框': '//*[@id="_easyui_textbox_input108"]',
    '地址输入提示': '#bodyLayout > div.panel.window.messager-panel.messager-window > div.panel-header.panel-header-noborder.window-header > div.panel-tool',
    '地址栏': '//*[@id="divBaseInfo1"]/div[2]/div/table/tbody/tr[6]',
    '安徽省': '//*[@id="_easyui_combobox_i33_4"]',
    '芜湖市': '//*[@id="_easyui_combobox_i49_0"]',
    '南陵县': '//*[@id="_easyui_combobox_i53_0"]',
    '籍山镇': '//*[@id="_easyui_combobox_i54_0"]',
    '和顺居委会': '//*[@id="_easyui_combobox_i55_0"]',
    '省份下拉按钮': '//*[@id="divBaseInfo1"]/div[2]/div/table/tbody/tr[6]/td[2]/span[1]/span',
    '城市下拉按钮': '//*[@id="divBaseInfo1"]/div[2]/div/table/tbody/tr[6]/td[2]/span[2]/span',
    '区域下拉按钮': '//*[@id="divBaseInfo1"]/div[2]/div/table/tbody/tr[6]/td[2]/span[3]/span',
    '街道下拉按钮': '//*[@id="divBaseInfo1"]/div[2]/div/table/tbody/tr[6]/td[2]/span[4]/span',
    '村委下拉按钮': '//*[@id="divBaseInfo1"]/div[2]/div/table/tbody/tr[6]/td[2]/span[5]/span',
    '详细地址栏': '//*[@id="divBaseInfo1"]/div[2]/div/table/tbody/tr[7]',
    '路输入框': '//*[@id="_easyui_textbox_input13"]',
    '弄输入框': '//*[@id="_easyui_textbox_input14"]',
    '号输入框': '//*[@id="_easyui_textbox_input15"]',
    '室输入框': '//*[@id="_easyui_textbox_input16"]',
    '关系输入框': '//*[@id="_easyui_textbox_input80"]',
    '家属姓名输入框': '//*[@id="_easyui_textbox_input22"]',
    '家属电话输入框': '//*[@id="_easyui_textbox_input141"]',
    '家属信息栏': '//*[@id="divBaseInfo1"]/div[2]/div/table/tbody/tr[10]',
    '关系下拉按钮': '//*[@id="divBaseInfo1"]/div[2]/div/table/tbody/tr[10]/td[2]/span[1]/span',
    '朋友': '//*[@id="_easyui_combobox_i6_43"]',
    '体检登记-单位输入框': '//*[@id="_easyui_textbox_input142"]',
    '部门输入框': '//*[@id="_easyui_textbox_input8"]',
    '邮箱输入框': '//*[@id="_easyui_textbox_input103"]',
    '单位信息栏': '//*[@id="divBaseInfo1"]/div[2]/div/table/tbody/tr[4]',
    '预约日期': '//*[@id="_easyui_textbox_input110"]',
    '预约日期日历': '//*[@id="divBaseInfo1"]/div[2]/div/table/tbody/tr[11]/td[2]/span[2]/span',
    '预约日期日历-日历下一月': '//*[@id="bodyLayout"]/div[54]/div/div[1]/div/div[1]/div[2]',
    '预约日期日历-日历具体日期': '//*[@id="bodyLayout"]/div[54]/div/div[1]/div/div[2]/table/tbody/tr[3]/td[4]',
    '纸质报告单状态栏': '//*[@id="divBaseInfo1"]/div[2]/div/table/tbody/tr[10]/td[2]/label',
    '勾选纸质报告单': '//*[@id="divBaseInfo1"]/div[2]/div/table/tbody/tr[10]/td[2]/label/input',
    '套餐项目信息栏': '//*[@id="tabUnSel"]',
    '项目列表': '//*[@id="tabUnSel"]/div[1]/div[3]/ul/li[2]',
    '套餐列表': '//*[@id="tabUnSel"]/div[1]/div[3]/ul/li[1]',
    '项目搜索框': '//*[@id="_easyui_textbox_input152"]',
    '项目搜索按钮': '//*[@id="tabUnSel"]/div[2]/div[2]/div/div/div/div[1]/table/tbody/tr/td[1]/span/span',
    '项目搜索结果': '//*[@id="tabUnSel"]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[2]/table[1]/tbody',
    '套餐信息表': '//*[@id="tabUnSel"]/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/table',
    '项目信息表': '//*[@id="tabUnSel"]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[2]/table[1]',
    '套餐搜索框': '//*[@id="_easyui_textbox_input151"]',
    '套餐搜索按钮': '//*[@id="tabUnSel"]/div[2]/div[1]/div/div/div/div[1]/table/tbody/tr/td[1]/span/span',
    '套餐搜索结果': '//*[@id="tabUnSel"]/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/table/tbody',
    '套餐1': '//*[@id="datagrid-row-r8-2-0"]/td[1]/div',
    '套餐2': '//*[@id="datagrid-row-r8-2-1"]/td[1]/div',
    '已选套餐信息栏': '//*[@id="tabSel"]/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div[1]',
    '套餐/项目选择键': '//*[@id="btnSelRegProject"]/span',
    '套餐/项目移除键': '//*[@id="btnUnSelRegProject"]/span',
    '确定替换套餐': '#bodyLayout > div.panel.window.messager-panel.messager-window > div.dialog-button.messager-button > a:nth-child(1)',
    '已选项目1勾选按钮': '//*[@id="datagrid-row-r10-2-0"]/td[1]/div/input',
    '确定移除项目': '#bodyLayout > div.panel.window.messager-panel.messager-window > div.dialog-button.messager-button > a:nth-child(1)',
    '已选项目1': '//*[@id="datagrid-row-r10-2-0"]/td[5]',
    '套餐/项目全部移除键': '#tabSel > div.tabs-panels.tabs-panels-noborder.panel-noscroll > div.panel.easyui-fluid > div > div > div > div.datagrid-view > div.datagrid-view2 > div.datagrid-body > div.datagrid-group > span.datagrid-group-title > a',
    '已选项目详细信息': '//*[@id="tabSel"]/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]',
    '套餐-项目全部移除键': '#tabSel > div.tabs-panels.tabs-panels-noborder.panel-noscroll > div.panel.easyui-fluid > div > div > div > div.datagrid-view > div.datagrid-view2 > div.datagrid-body > div.datagrid-group > span.datagrid-group-title > a',
    '替换套餐-移除项目、套餐确认键': '#bodyLayout > div.panel.window.messager-panel.messager-window > div.dialog-button.messager-button > a:nth-child(1)',
    '项目1': '//*[@id="datagrid-row-r9-2-0"]/td[2]',
    '项目2': '//*[@id="datagrid-row-r9-2-1"]/td[2]',
    '项目3': '//*[@id="datagrid-row-r9-2-2"]/td[2]',
    '项目4': '//*[@id="datagrid-row-r9-2-3"]/td[2]',
    '项目5': '//*[@id="datagrid-row-r9-2-4"]/td[2]',
    '项目6': '//*[@id="datagrid-row-r9-2-5"]/td[2]',
    '费用信息详情': '//*[@id="divSelProject"]/div[2]',
    '套餐-项目选择键': '//*[@id="btnSelRegProject"]/span',
    '套餐-项目移除键': '//*[@id="btnUnSelRegProject"]/span',
    '体检登记-保存': '//*[@id="btnSave"]',
    '输入提示': '#bodyLayout > div.panel.window.messager-panel.messager-window > div.panel-header.panel-header-noborder.window-header > div.panel-tool',
    '体检登记管理-删除': '//*[@id="btnDel"]',
    '体检登记管理-确认删除': '//*[@id="btnOk"]',
    '体检登记-关闭确认': '#bodyLayout > div.panel.window.messager-panel.messager-window > div.dialog-button.messager-button > a:nth-child(1)',
    '绑定批次下拉按钮': '//*[@id="regionDisplayAll"]/div/label[1]/span/span/a[2]',
    '第一个批次': '//*[@id="datagrid-row-r3-2-0"]',
    '绑定批次信息栏': '//*[@id="regionDisplayAll"]/div/label[1]/span',
    '预约团队下拉按钮': '//*[@id="formSearch"]/table/tbody/tr[2]/td[6]/span[1]/span/a[2]',
    '预约团队搜索框': '//*[@id="_easyui_textbox_input49"]',
    '批次勾选': '//*[@id="bodyLayout"]/div[17]/div/div/div/div[2]/div[2]/div[1]/div/table/tbody/tr/td[2]/div/input',
    '批次选项关闭': '//*[@id="bodyLayout"]/div[17]/div/div/div/div[1]/table/tbody/tr/td[3]',
    '体检登记管理-搜索': '//*[@id="btnSearch"]/span/span',
    '慢性病输入框': '//*[@id="_easyui_textbox_input143"]',
    '医保险种下拉框': '//*[@id="divBaseInfo1"]/div[2]/div/table/tbody/tr[8]/td[2]/span[3]/span/a',
    '医保险种1': '//*[@id="_easyui_combobox_i12_0"]',
    '医保险种2': '//*[@id="_easyui_combobox_i12_1"]',
    '医保险种信息栏': '//*[@id="_easyui_textbox_input86"]',
    '体检登记管理（大标）': '//*[@id="divHome"]/div/ul[1]/li[4]',
    '体检登记管理页面': '//*[@id="divMainCenter"]/div[1]/div/div',
    '关闭体检签到': '//*[@id="tabs"]/div[1]/div[3]/ul/li[2]/a[2]',
}


class Registration(SignIn):
    def __init__(self, business, product, browser):
        self.xpath_dict = business_xpath_dict
        self.driver = Sign(product, self.xpath_dict, browser).driver
        if business == '体检登记':
            self.pe_registration()

    def pe_registration(self):
        self.driver.click_ele('体检登记')
        self.driver.driver.switch_to.frame(0)
        try:
            self.driver.click_ele('HIS提示确定', By.CSS_SELECTOR)
            # self.driver.click_ele('HIS提示确定', By.)
        except:
            pass
        assert '新登记' in self.driver.text_ele('体检登记页面'), '进入登记失败'

    # 签到验证完成后取消签到
    def cancel_sign_in(self, number1=None, number2=None, business=None, batch_name=None):
        self.driver.driver.switch_to.default_content()
        try:
            self.driver.click_ele('关闭体检签到')
            self.driver.click_ele('体检登记-关闭确认', By.CSS_SELECTOR)
        except:
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
        self.driver.continuous_clicks('{}：{}|登记人员照片'.format(locate_value, input_value))

    def address_input(self, province, city, region, neighborhood, village, input_type=None):
        if input_type is None:
            self.driver.set_empty('省份输入框')
            self.driver.input_ele('省份输入框', province)
            self.driver.input_ele('城市输入框', city)
            self.driver.input_ele('区域输入框', region)
            self.driver.input_ele('街道输入框', neighborhood)
            exists = self.driver.exists_judge('地址输入提示', By.CSS_SELECTOR)
            if exists is True:
                self.driver.click_ele('地址输入提示', By.CSS_SELECTOR)
            self.driver.input_ele('村委输入框', village)
            result = province and city and region and neighborhood and village in self.driver.text_recognition('地址栏')
        else:
            self.driver.continuous_clicks('省份下拉按钮|{}'.format(province))
            exists = self.driver.exists_judge('地址输入提示', By.CSS_SELECTOR)
            if exists is True:
                self.driver.click_ele('地址输入提示', By.CSS_SELECTOR)
            self.driver.continuous_clicks('城市下拉按钮|{}'.format(city))
            self.driver.continuous_clicks('区域下拉按钮|{}'.format(region))
            self.driver.continuous_clicks('街道下拉按钮|{}'.format(neighborhood))
            if exists is True:
                self.driver.click_ele('地址输入提示', By.CSS_SELECTOR)
            self.driver.continuous_clicks('村委下拉按钮|{}'.format(village))
            result = province and city and region and neighborhood and village in self.driver.text_recognition('地址栏')
        return result

    def full_address_input(self, road, lane, number, room):
        self.driver.input_ele('路输入框', road)
        self.driver.input_ele('弄输入框', lane)
        self.driver.input_ele('号输入框', number)
        self.driver.input_ele('室输入框', room)
        result = road and lane and number and room in self.driver.text_recognition('详细地址栏')
        return result

    def families_info_input(self, relation, name, phone_number, input_type=None):
        if input_type is None:
            self.driver.input_ele('关系输入框', relation)
            self.driver.input_ele('家属姓名输入框', name)
            self.driver.input_ele('家属电话输入框', phone_number)
        elif input_type == '下拉点击':
            self.driver.set_empty('关系输入框')
            self.driver.click_ele(relation)
            self.driver.continuous_clicks('关系下拉按钮|{}'.format(relation))
        result = relation and name and phone_number in self.driver.text_recognition('家属信息栏')
        return result

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

    def single_items_check(self, number):
        expense1 = '1'
        expense2 = '1'
        for i in range(1, int(number) + 1):
            item1 = self.driver.text_recognition('已选项目详细信息')
            self.driver.continuous_double_clicks('项目列表|项目{}'.format(i))
            if i == 1:
                expense1 = self.driver.text_recognition('费用信息详情')
            if i == number:
                expense2 = self.driver.text_recognition('费用信息详情')
            item2 = self.driver.text_recognition('已选项目详细信息')
            assert item1 != item2
        result = expense1 != expense2
        return result
