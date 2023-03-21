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
    '体检签到': '//*[@id="divHome"]/div/ul[1]/li[6]',
    '签到页面': '//*[@id="btnSign"]',
    '全部批次选项': '//*[@id="formSearch"]/table/tbody/tr[2]/td[4]/span[1]/span',
    '有人批次': '//*[@id="datagrid-row-r4-2-2"]',
    '批次3': '//*[@id="datagrid-row-r4-2-2"]',
    '无人批次': '//*[@id="datagrid-row-r4-2-9"]',
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
    '单位：测试X': '//*[@id="_easyui_combobox_i8_3"]',
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
    '套餐-项目选择键': '//*[@id="btnSelRegProject"]/span',
    '套餐-项目移除键': '//*[@id="btnUnSelRegProject"]/span',
    '确定替换套餐': '#bodyLayout > div.panel.window.messager-panel.messager-window > div.dialog-button.messager-button > a:nth-child(1)',
    '已选项目1勾选按钮': '//*[@id="datagrid-row-r10-2-0"]/td[1]/div/input',
    '确定移除项目': '#bodyLayout > div.panel.window.messager-panel.messager-window > div.dialog-button.messager-button > a:nth-child(1)',
    '已选项目1': '//*[@id="datagrid-row-r10-2-0"]/td[5]',
    '套餐-项目全部移除键': '#tabSel > div.tabs-panels.tabs-panels-noborder.panel-noscroll > div.panel.easyui-fluid > div > div > div > div.datagrid-view > div.datagrid-view2 > div.datagrid-body > div.datagrid-group > span.datagrid-group-title > a',
    '已选项目详细信息': '//*[@id="tabSel"]/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]',
    '替换套餐-移除项目、套餐确认键': '#bodyLayout > div.panel.window.messager-panel.messager-window > div.dialog-button.messager-button > a:nth-child(1)',
    '项目1': '//*[@id="datagrid-row-r9-2-0"]/td[2]',
    '项目2': '//*[@id="datagrid-row-r9-2-1"]/td[2]',
    '项目3': '//*[@id="datagrid-row-r9-2-2"]/td[2]',
    '项目4': '//*[@id="datagrid-row-r9-2-3"]/td[2]',
    '项目5': '//*[@id="datagrid-row-r9-2-4"]/td[2]',
    '项目6': '//*[@id="datagrid-row-r9-2-5"]/td[2]',
    '费用信息详情': '//*[@id="divSelProject"]/div[2]',
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
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',

    '': '#bodyLayout > div:nth-child(91)',
    '': '#bodyLayout > div:nth-child(94)',
    '': '330702197705156021',

}


class Business(object):
    def __init__(self, business, product, browser):
        self.xpath_dict = business_xpath_dict
        self.driver = Sign(product, self.xpath_dict, browser).driver
        if business == '体检签到':
            self.pe_sign_in()
        elif business == '体检登记':
            self.pe_registration()
        elif business == '科室检查':
            self.pe_department_inspection()

    def pe_sign_in(self):
        self.driver.click_ele('体检签到')
        self.driver.driver.switch_to.frame(0)
        assert '签到' in self.driver.text_ele('签到页面'), '进入签到失败'

    def pe_registration(self):
        self.driver.click_ele('体检登记')
        self.driver.driver.switch_to.frame(0)
        try:
            self.driver.click_ele('HIS提示确定', By.CSS_SELECTOR)
            # self.driver.click_ele('HIS提示确定', By.)
        except:
            pass
        assert '新登记' in self.driver.text_ele('体检登记页面'), '进入登记失败'

    def pe_department_inspection(self):
        self.driver.click_ele('科室检查')
        self.driver.driver.switch_to.frame(0)
        assert '检查科室' in self.driver.text_ele('科室检查页面'), '进入签到失败'

    def pe_registration_manage(self):
        self.driver.click_ele('体检登记管理')
        self.driver.driver.switch_to.frame(0)
        assert '打印导检单' in self.driver.text_ele('体检登记管理页面'), '进入登记失败'

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

    def cancel_check(self):
        # self.account_check()
        self.driver.continuous_clicks('体检人员列表-编号输入框：202105281325')
        # self.driver.continuous_clicks('科室检查-开始日期|科室检查-开始日期向前一月|科室检查-开始具体日期|科室检查-搜索')
        # self.driver.continuous_clicks('科室检查-已检|')
    '202105281325'
