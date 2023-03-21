import os.path
import pytest
import allure
# from WEB_UI_TEST.business_methods.peis import Business
from WEB_UI_TEST.business_methods.pe_sign_in import SignIn
from selenium.webdriver.common.by import By
from WEB_UI_TEST.public_methods.same_use import *


@allure.epic('健康管理系统')
@allure.feature('体检签到-登记时间')
@allure.story('正确时间范围，有搜索结果')
def test_pe_signin_case1():
    browser = SignIn('体检签到', 'peis', 'Chrome').driver
    browser.continuous_clicks('全部批次选项|有人批次|批次确定|搜索')
    assert len(browser.text_ele('搜索结果')) != 0, '正确时间，有结果校验失败'


@allure.epic('健康管理系统')
@allure.feature('体检签到-登记时间')
@allure.story('正确时间范围，无搜索结果')
def test_pe_signin_case2():
    browser = SignIn('体检签到', 'peis', 'Chrome').driver
    browser.continuous_clicks('全部批次选项|无人批次|批次确定|搜索')
    assert '没有搜索到相关登记记录' in browser.text_ele('提示'), '正确时间，无结果校验失败'


@allure.epic('健康管理系统')
@allure.feature('体检签到-登记时间')
@allure.story('错误时间范围搜索')
def test_pe_signin_case3():
    browser = SignIn('体检签到', 'peis', 'Chrome').driver
    browser.continuous_clicks('登记结束日期|结束日期向前一年|日期中间日|搜索')
    assert '不可大于结束' in browser.text_ele('日期范围提示', By.CSS_SELECTOR), '错误时间范围搜索校验失败'


@allure.epic('健康管理系统')
@allure.feature('体检登记')
@allure.story('体检类型检查及功能确认')
def test_pe_signin_case4():
    browser = SignIn('体检签到', 'peis', 'Chrome').driver
    browser.continuous_clicks('全部批次选项|批次3|批次确定')
    for i in range(1, 16):
        browser.continuous_clicks('体检类型下拉按钮|体检类型{}'.format(i))
        if i == 1:
            browser.click_ele('搜索')
            assert browser.text_ele('搜索结果') is not None
        elif i == 2:
            browser.click_ele('搜索')
            assert '没有搜索到相关登记记录' in browser.text_ele('提示')
        pic = pic_save()
        browser.ele_location(locate_value='体检类型下拉按钮').screenshot(pic)
        type_list = ['全部', '常规体检', '出入境体检', '婚姻检查', '健康证', '两痘筛查/两癌筛查', '学生体检', '医保', '幼儿体检',
                     '职业病体检', '健康检查', '医共体专用', '职工体检', '多图报告', '驾照体检', '健康证类型']
        assert ocr(pic) in type_list[i]
        os.remove(pic)


@allure.epic('健康管理系统')
@allure.feature('体检签到-单位')
@allure.story('手动输入单位')
def test_pe_signin_case5():
    browser = SignIn('体检签到', 'peis', 'Chrome').driver
    browser.continuous_clicks('单位输入框：有信用代码|有信用代码|搜索')
    yes_result = browser.text_ele('搜索结果') is not None
    browser.continuous_clicks('单位输入框：无信用代码|无信用代码|搜索')
    no_result = '没有搜索到相关登记记录' in browser.text_ele('提示')
    assert yes_result is True and no_result is True, '手动输入单位进行搜索，校验失败'


@allure.epic('健康管理系统')
@allure.feature('体检签到-单位')
@allure.story('下拉选择单位')
def test_pe_signin_case6():
    browser = SignIn('体检签到', 'peis', 'Chrome').driver
    browser.continuous_clicks('单位下拉选择按钮|有信用代码|搜索')
    yes_result = browser.text_ele('搜索结果') is not None
    browser.continuous_clicks('单位下拉选择按钮|无信用代码|搜索')
    no_result = '没有搜索到相关登记记录' in browser.text_ele('提示')
    assert yes_result is True and no_result is True, '下拉选择单位进行搜索，校验失败'


@allure.epic('健康管理系统')
@allure.feature('体检签到-批次')
@allure.story('手工输入批次')
def test_pe_signin_case7():
    browser = SignIn('体检签到', 'peis', 'Chrome').driver
    browser.continuous_clicks('批次下拉选择按钮|批次输入框：大V发地方是|批次搜索按钮|批次搜索结果|批次确定|搜索')
    assert '没有搜索到相关登记记录' in browser.text_ele('提示'), '手工输入批次无搜索结果，校验失败'


@allure.epic('健康管理系统')
@allure.feature('体检签到-证件编号')
@allure.story('证件编号搜索')
def test_pe_signin_case8():
    browser = SignIn('体检签到', 'peis', 'Chrome').driver
    browser.continuous_clicks('证件编号输入框：330120199101010012|搜索')
    yes_result = '330120199101010012' in browser.text_ele('证件编号')
    browser.continuous_clicks('证件编号输入框：3|搜索')
    no_result = '没有搜索到相关登记记录' in browser.text_ele('提示')
    assert yes_result is True and no_result is True, '证件编号搜索，校验失败'


@allure.epic('健康管理系统')
@allure.feature('体检签到-姓名')
@allure.story('姓名搜索')
def test_pe_signin_case9():
    browser = SignIn('体检签到', 'peis', 'Chrome').driver
    browser.continuous_clicks('姓名输入框：王磊|搜索')
    yes_result = '370628197910296512' in browser.text_ele('证件编号')
    browser.continuous_clicks('姓名输入框：3|搜索')
    no_result = '没有搜索到相关登记记录' in browser.text_ele('提示')
    assert yes_result is True and no_result is True, '姓名搜索，校验失败'


@allure.epic('健康管理系统')
@allure.feature('体检签到-组合条件')
@allure.story('组合条件搜索')
def test_pe_signin_case10():
    browser = SignIn('体检签到', 'peis', 'Chrome').driver
    browser.continuous_clicks('单位输入框：youdi团队|姓名输入框：贺琳|证件编号输入框：130324196309198523|体检类型下拉按钮|体检类型9|搜索')
    yes_result = '130324196309198523' in browser.text_ele('证件编号')
    browser.continuous_clicks('姓名输入框：3|搜索')
    no_result = '没有搜索到相关登记记录' in browser.text_ele('提示')
    assert yes_result is True and no_result is True, '组合条件搜索，校验失败'


@allure.epic('健康管理系统')
@allure.feature('体检签到-前n行签到')
@allure.story('点勾')
def test_pe_signin_case11():
    browser = SignIn('体检签到', 'peis', 'Chrome')
    browser.driver.continuous_clicks('单位下拉选择按钮|单位:测试X|体检类型下拉按钮|体检类型9|搜索')
    register_number1 = browser.driver.text_ele('登记编号1')
    register_number2 = browser.driver.text_ele('登记编号2')
    browser.driver.continuous_clicks('目标行输入框：2|目标行确认|签到')
    assert '签到成功' in browser.driver.text_ele('提示')
    browser.cancel_sign_in(register_number1, register_number2)


@allure.epic('健康管理系统')
@allure.feature('体检签到-前n行签到')
@allure.story('数字不合法')
def test_pe_signin_case12():
    browser = SignIn('体检签到', 'peis', 'Chrome').driver
    browser.continuous_clicks('目标行输入框：2.5|目标行确认')
    assert '请输入整数' in browser.text_ele('提示')


@allure.epic('健康管理系统')
@allure.feature('体检签到-前n行签到')
@allure.story('无搜索结果')
def test_pe_signin_case13():
    browser = SignIn('体检签到', 'peis', 'Chrome').driver
    browser.click_ele('签到')
    assert '请先选择签到人员' in browser.text_ele('提示')


@allure.epic('健康管理系统')
@allure.feature('体检签到-前n行签到')
@allure.story('手动选择')
def test_pe_signin_case14():
    browser = SignIn('体检签到', 'peis', 'Chrome')
    browser.driver.continuous_clicks('单位下拉选择按钮|单位:测试X|体检类型下拉按钮|体检类型9|搜索')
    register_number1 = browser.driver.text_ele('登记编号1')
    register_number2 = browser.driver.text_ele('登记编号2')
    browser.driver.continuous_clicks('勾选搜索结果|签到')
    assert '签到成功' in browser.driver.text_ele('提示')
    browser.cancel_sign_in(register_number1, register_number2)


if __name__ == '__main__':
    pytest.main(["-s", "-v"])
