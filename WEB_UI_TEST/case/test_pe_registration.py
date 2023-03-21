import pytest
import allure
from WEB_UI_TEST.business_methods.pe_registration import Registration
from selenium.webdriver.common.by import By
from WEB_UI_TEST.public_methods.same_use import *


@allure.epic('健康管理系统')
@allure.feature('体检登记-新登记')
@allure.story('手动输入正确身份证')
def test_pe_registration_case1():
    browser = Registration('体检登记', 'peis', 'Chrome')
    browser.input_move_focus('证件输入框', '330702197705156021')
    result1 = '1977-05-15' in browser.driver.text_recognition('出生日期输入框')
    result2 = browser.driver.text_recognition('年龄') is not None
    result3 = browser.driver.text_recognition('性别切换') is not None
    result_list = [result1, result2, result3]
    assert False not in result_list, '手动输入正确身份证，校验失败'


@allure.epic('健康管理系统')
@allure.feature('体检登记-新登记')
@allure.story('手动输入长度错误身份证')
def test_pe_registration_case2():
    browser = Registration('体检登记', 'peis', 'Chrome')
    browser.input_move_focus('证件输入框', '3307021977051560211')
    assert '请输入正确的身份证号' in browser.driver.text_ele('提示'), '手动输入长度错误身份证，校验失败'


@allure.epic('健康管理系统')
@allure.feature('体检登记-新登记')
@allure.story('手动输入格式错误身份证')
def test_pe_registration_case3():
    browser = Registration('体检登记', 'peis', 'Chrome')
    browser.input_move_focus('证件输入框', '我的身份证')
    assert '请输入正确的身份证号' in browser.driver.text_ele('提示'), '手动输入格式错误身份证，校验失败'


@allure.epic('健康管理系统')
@allure.feature('体检登记-新登记')
@allure.story('体检类型选择及确认')
def test_pe_registration_case4():
    browser = Registration('体检登记', 'peis', 'Chrome')
    result = browser.type_check('体检类型', '15')
    assert result is True, '体检类型选择及确认,校验失败'


@allure.epic('健康管理系统')
@allure.feature('体检登记-新登记')
@allure.story('健康证扩展信息输入')
def test_pe_registration_case5():
    browser = Registration('体检登记', 'peis', 'Chrome')
    result = browser.type_check('健康类别', '8')
    assert result is True, '健康证扩展信息输入,校验失败'


@allure.epic('健康管理系统')
@allure.feature('体检登记-文化')
@allure.story('文化框功能')
def test_pe_registration_case6():
    browser = Registration('体检登记', 'peis', 'Chrome')
    result = browser.type_check('文化类别', '7')
    assert result is True, '文化框功能,校验失败'


@allure.epic('健康管理系统')
@allure.feature('体检登记-出生日期')
@allure.story('输入格式正确的出生日期')
def test_pe_registration_case7():
    browser = Registration('体检登记', 'peis', 'Chrome')
    browser.input_move_focus('出生日期输入框', '1999')
    assert browser.driver.text_recognition('年龄') is not None, '输入格式正确的出生日期,校验失败'
    

@allure.epic('健康管理系统')
@allure.feature('体检登记-出生日期')
@allure.story('输入格式错误的出生日期')
def test_pe_registration_case8():
    browser = Registration('体检登记', 'peis', 'Chrome')
    browser.input_move_focus('出生日期输入框', '9999')
    assert '出生日期不可大于当前日期' in browser.driver.text_ele('提示'), '输入格式错误的出生日期,校验失败'


@allure.epic('健康管理系统')
@allure.feature('体检登记-出生日期')
@allure.story('点击日历选择时间')
def test_pe_registration_case9():
    browser = Registration('体检登记', 'peis', 'Chrome').driver
    browser.continuous_clicks('出生日期日历|日历前一年|日历前一月|日历具体日期')
    assert browser.text_recognition('年龄') is not None, '点击日历选择时间,校验失败'
    

@allure.epic('健康管理系统')
@allure.feature('体检登记-输入年龄')
@allure.story('年龄输入校验')
def test_pe_registration_case10():
    browser = Registration('体检登记', 'peis', 'Chrome')
    browser.input_move_focus('年龄输入框', '20')
    assert browser.driver.text_recognition('出生日期输入框') is not None, '输入格式正确的出生日期,校验失败'
    browser.driver.set_empty('年龄输入框')
    browser.driver.input_ele('年龄输入框', '-0.5')
    assert '请输入整数' in browser.driver.text_recognition('年龄输入提示'), '输入格式错误的出生日期,校验失败'
    

@allure.epic('健康管理系统')
@allure.feature('体检登记-输入姓名')
@allure.story('姓名输入校验')
def test_pe_registration_case11():
    browser = Registration('体检登记', 'peis', 'Chrome')
    browser.input_move_focus('体检登记姓名输入框', '奥特曼')
    assert '奥特曼' in browser.driver.text_recognition('体检登记姓名输入框'), '姓名输入,校验失败'
    browser.driver.set_empty('体检登记姓名输入框')
    browser.input_move_focus('体检登记姓名输入框', '  ')
    browser.driver.mouse_hover('体检登记姓名输入框')
    assert '该输入项为必输项' in browser.driver.text_recognition('姓名行'), '姓名输入,校验失败'
    

@allure.epic('健康管理系统')
@allure.feature('体检登记-性别切换')
@allure.story('性别切换验证')
def test_pe_registration_case12():
    browser = Registration('体检登记', 'peis', 'Chrome')
    result1 = browser.driver.text_recognition('性别切换')
    browser.driver.continuous_clicks('性别切换|性别女')
    result2 = browser.driver.text_recognition('性别切换')
    assert result1 != result2, '性别切换验证，校验失败'
    

@allure.epic('健康管理系统')
@allure.feature('体检登记-电话输入')
@allure.story('电话输入校验')
def test_pe_registration_case13():
    browser = Registration('体检登记', 'peis', 'Chrome')
    browser.input_move_focus('电话输入框', '15062066666')
    right_result = '15062066666' in browser.driver.text_recognition('电话输入框')
    browser.input_move_focus('电话输入框', '6')
    wrong_result = '请输入正确的联系电话' in browser.driver.text_ele('提示')
    assert right_result is True and wrong_result is True


@allure.epic('健康管理系统')
@allure.feature('体检登记-婚姻')
@allure.story('婚姻栏检查')
def test_pe_registration_case14():
    browser = Registration('体检登记', 'peis', 'Chrome')
    result = browser.type_check('婚姻类别', '7')
    assert result is True, '文化框功能,校验失败'


@allure.epic('健康管理系统')
@allure.feature('体检登记-地址')
@allure.story('地址不同方式输入功能确认')
def test_pe_registration_case15():
    browser = Registration('体检登记', 'peis', 'Chrome')
    result1 = browser.address_input('江苏省', '南京市', '建邺区', '沙洲街道', '双和园')
    result2 = browser.address_input('安徽省', '芜湖市', '南陵县', '籍山镇', '和顺居委会', '下拉点击输入')
    print(result1, result2)
    assert result1 is True and result2 is True


@allure.epic('健康管理系统')
@allure.feature('体检登记-详细地址')
@allure.story('详细地址输入功能确认')
def test_pe_registration_case16():
    browser = Registration('体检登记', 'peis', 'Chrome')
    result = browser.full_address_input('友谊街', '六十七弄', '四号', '1805')
    assert result is True


@allure.epic('健康管理系统')
@allure.feature('体检登记-家属')
@allure.story('家属信息输入功能确认')
def test_pe_registration_case17():
    browser = Registration('体检登记', 'peis', 'Chrome')
    right_result1 = browser.families_info_input('儿子', '狗蛋', '15062066666')
    right_result2 = browser.families_info_input('朋友', '狗蛋', '15062066666', '下拉点击')
    browser.input_move_focus('家属电话输入框', '6')
    wrong_result = '请输入正确的联系电话' in browser.driver.text_ele('提示')
    assert right_result1 is True and right_result2 is True and wrong_result is True


@allure.epic('健康管理系统')
@allure.feature('体检登记-单位、部门、邮箱')
@allure.story('单位信息栏输入功能确认')
def test_pe_registration_case18():
    browser = Registration('体检登记', 'peis', 'Chrome')
    browser.continuous_input('体检登记-单位输入框', '保密单位', '部门输入框', '保密部门', '邮箱输入框', '163@163.com')
    right_result = '保密单位' and '保密部门' and '163@163.com' in browser.driver.text_recognition('单位信息栏')
    browser.driver.input_ele('邮箱输入框', '.')
    browser.driver.mouse_hover('邮箱输入框')
    wrong_result = '请输入正确的' in browser.driver.text_recognition('单位信息栏')
    assert right_result is True and wrong_result is True


@allure.epic('健康管理系统')
@allure.feature('体检登记-预约时间')
@allure.story('预约时间栏功能确认')
def test_pe_registration_case19():
    browser = Registration('体检登记', 'peis', 'Chrome')
    default_date = browser.driver.text_recognition('预约日期')
    now_date = time.strftime("%Y-%m-%d", time.localtime())
    result1 = default_date == now_date
    browser.driver.continuous_clicks('预约日期日历|预约日期日历-日历下一月|预约日期日历-日历具体日期')
    result2 = browser.driver.text_recognition('预约日期') is not None
    assert result1 is True and result2 is True, '预约时间栏功能确认，校验失败'


@allure.epic('健康管理系统')
@allure.feature('体检登记-纸质报告单')
@allure.story('勾选纸质报告单功能确认')
def test_pe_registration_case20():
    browser = Registration('体检登记', 'peis', 'Chrome')
    default_result = '√' not in browser.driver.text_recognition('家属信息栏')
    browser.driver.click_ele('勾选纸质报告单')
    tick_result = '√' in browser.driver.text_recognition('家属信息栏')
    assert default_result is True and tick_result is True


@allure.epic('健康管理系统')
@allure.feature('体检登记-套餐、项目切换')
@allure.story('套餐、项目列表切换')
def test_pe_registration_case21():
    browser = Registration('体检登记', 'peis', 'Chrome')
    default_result = '套餐名称' in browser.driver.text_recognition('套餐项目信息栏')
    browser.driver.click_ele('项目列表')
    switch_result = '项目名称' in browser.driver.text_recognition('套餐项目信息栏')
    assert default_result is True and switch_result is True


@allure.epic('健康管理系统')
@allure.feature('体检登记-项目搜索')
@allure.story('项目搜索功能校验')
def test_pe_registration_case22():
    browser = Registration('体检登记', 'peis', 'Chrome')
    browser.driver.continuous_clicks('项目列表|项目搜索框：未婚项目|项目搜索按钮')
    click_search_result = '未婚项目' in browser.driver.text_recognition('项目搜索结果')
    browser.driver.set_empty('项目搜索框')
    delete_result = '默认绑定' in browser.driver.text_recognition('项目搜索结果')
    browser.driver.continuous_clicks('项目列表|项目搜索框：已婚项目')
    keyboard_search_result = '已婚项目' in browser.driver.text_recognition('项目搜索结果')
    result_list = [click_search_result, delete_result, keyboard_search_result]
    assert False not in result_list, '项目搜索功能，校验失败'


@allure.epic('健康管理系统')
@allure.feature('体检登记-套餐/单项性别校验')
@allure.story('套餐/单项性别校验')
def test_pe_registration_case23():
    browser = Registration('体检登记', 'peis', 'Chrome')
    default_result1 = '女' not in browser.get_target_data('套餐信息表', '4')
    browser.driver.click_ele('项目列表')
    default_result2 = '女' not in browser.get_target_data('项目信息表', '4')
    browser.driver.continuous_clicks('性别切换|性别女')
    switch_result1 = '男' not in browser.get_target_data('项目信息表', '4')
    browser.driver.click_ele('套餐列表')
    switch_result2 = '男' not in browser.get_target_data('套餐信息表', '4')
    result_list = [default_result1, default_result2, switch_result1, switch_result2]
    assert False not in result_list


@allure.epic('健康管理系统')
@allure.feature('体检登记-套餐搜索')
@allure.story('套餐搜索功能校验')
def test_pe_registration_case24():
    browser = Registration('体检登记', 'peis', 'Chrome')
    browser.driver.continuous_clicks('套餐列表|套餐搜索框：冰封测试|套餐搜索按钮')
    click_search_result = '冰封测试' in browser.driver.text_recognition('套餐搜索结果')
    browser.driver.set_empty('套餐搜索框')
    delete_result = '企业退休人员体检' in browser.driver.text_ele('套餐搜索结果')
    browser.driver.continuous_clicks('套餐列表|套餐搜索框：未婚专享')
    keyboard_search_result = '未婚专享' in browser.driver.text_recognition('套餐搜索结果')
    result_list = [click_search_result, delete_result, keyboard_search_result]
    assert False not in result_list, '套餐搜索功能，校验失败'


@allure.epic('健康管理系统')
@allure.feature('体检登记-套餐')
@allure.story('套餐选择、替换、删除功能校验')
def test_pe_registration_case25():
    browser = Registration('体检登记', 'peis', 'Chrome')
    browser.driver.input_ele('年龄输入框', '20')
    text1 = browser.driver.text_ele('套餐1')
    browser.driver.double_click('套餐1')
    result1 = text1 in browser.driver.text_ele('已选套餐信息栏')
    text2 = browser.driver.text_ele('套餐2')
    browser.driver.continuous_clicks('套餐2|套餐-项目选择键')
    browser.driver.click_ele('确定替换套餐', By.CSS_SELECTOR)
    result2 = text2 in browser.driver.text_ele('已选套餐信息栏')
    text3 = browser.driver.text_ele('已选项目1')
    browser.driver.continuous_clicks('已选项目1勾选按钮|套餐-项目移除键')
    browser.driver.click_ele('确定移除项目', By.CSS_SELECTOR)
    result3 = text3 not in browser.driver.text_ele('已选项目1')
    browser.driver.continuous_clicks('套餐-项目全部移除键/css|替换套餐-移除项目、套餐确认键/css')
    result4 = len(browser.driver.text_recognition('已选项目详细信息')) == 0
    result_list = [result1, result2, result3, result4]
    assert False not in result_list, '套餐选择、替换、删除功能，校验失败'


@allure.epic('健康管理系统')
@allure.feature('体检登记-项目')
@allure.story('项目选择、替换、删除功能校验')
def test_pe_registration_case26():
    browser = Registration('体检登记', 'peis', 'Chrome')
    browser.driver.click_ele('项目列表')
    text1 = browser.driver.text_ele('项目1')
    browser.driver.double_click('项目1')
    result1 = text1 in browser.driver.text_ele('已选项目详细信息')
    text2 = browser.driver.text_ele('项目2')
    browser.driver.continuous_clicks('项目2|套餐-项目选择键')
    result2 = text2 in browser.driver.text_ele('已选项目详细信息')
    browser.driver.double_click('已选项目1')
    browser.driver.continuous_clicks('已选项目1勾选按钮|套餐-项目移除键')
    result3 = len(browser.driver.text_recognition('已选项目详细信息')) == 0
    result_list = [result1, result2, result3]
    assert False not in result_list, '套餐选择、替换、删除功能，校验失败'


@allure.epic('健康管理系统')
@allure.feature('体检登记-项目')
@allure.story('连续增加多个单项及多项删除')
def test_pe_registration_case27():
    browser = Registration('体检登记', 'peis', 'Chrome')
    result = browser.single_items_check(6)
    assert result is True


@allure.epic('健康管理系统')
@allure.feature('体检登记-套餐')
@allure.story('连续增加多个套餐')
def test_pe_registration_case28():
    browser = Registration('体检登记', 'peis', 'Chrome')
    browser.driver.input_ele('年龄输入框', '20')
    text1 = browser.driver.text_ele('套餐1')
    browser.driver.continuous_clicks('项目列表|项目搜索框：血压体重|项目搜索结果|套餐-项目选择键'
                                     '|套餐列表|套餐1|套餐-项目选择键')
    browser.driver.click_ele('替换套餐-移除项目、套餐确认键', By.CSS_SELECTOR)
    result1 = text1 in browser.driver.text_ele('已选套餐信息栏')
    browser.driver.double_click('套餐2')
    result2 = browser.driver.exists_judge('替换套餐-移除项目、套餐确认键', By.CSS_SELECTOR)
    assert result1 is True and result2 is True


@allure.epic('健康管理系统')
@allure.feature('体检登记-套餐')
@allure.story('连续增加多个套餐')
def test_pe_registration_case29():
    browser = Registration('体检登记', 'peis', 'Chrome')
    browser.driver.continuous_clicks('体检登记姓名输入框：张三|体检登记-保存')
    assert '张三' in browser.driver.text_recognition('体检登记姓名输入框')
    browser.driver.click_ele('输入提示', By.CSS_SELECTOR)
    browser.driver.set_empty('体检登记姓名输入框')
    browser.driver.continuous_clicks('年龄输入框：20|体检登记-保存')
    assert '20' in browser.driver.text_recognition('年龄输入框')
    browser.driver.click_ele('输入提示', By.CSS_SELECTOR)
    browser.driver.set_empty('年龄输入框')
    browser.driver.double_click('套餐1')
    browser.driver.click_ele('输入提示', By.CSS_SELECTOR)
    browser.driver.continuous_clicks('体检登记姓名输入框：张三|年龄输入框：20')
    browser.driver.continuous_double_clicks('套餐2|体检登记-保存')
    browser.driver.ele_location(By.CSS_SELECTOR, locate_value='输入提示')
    assert '保存成功' in browser.driver.text_ele('提示')
    browser.cancel_sign_in(business='sign_in')


@allure.epic('健康管理系统')
@allure.feature('体检登记-绑定批次')
@allure.story('绑定批次、慢性病、医保保存')
def test_pe_registration_case30():
    browser = Registration('体检登记', 'peis', 'Chrome')
    browser.driver.continuous_clicks('体检登记姓名输入框：怪兽|年龄输入框：20|绑定批次下拉按钮')
    text = browser.driver.text_ele('第一个批次')
    browser.driver.click_ele('第一个批次')
    result1 = browser.driver.text_recognition('绑定批次信息栏') in text
    browser.driver.input_ele('慢性病输入框', '奥特曼恐惧症')
    result2 = '奥特曼恐惧症' in browser.driver.text_recognition('慢性病输入框')
    browser.driver.click_ele('医保险种下拉框')
    insurance1 = browser.driver.text_ele('医保险种1')
    browser.driver.click_ele('医保险种1')
    result3 = browser.driver.text_ele('医保险种信息栏') in insurance1
    browser.driver.click_ele('医保险种下拉框')
    insurance2 = browser.driver.text_ele('医保险种2')
    browser.driver.click_ele('医保险种2')
    result4 = browser.driver.text_ele('医保险种信息栏') in insurance2
    browser.driver.click_ele('体检登记-保存')
    result5 = '保存成功' in browser.driver.text_ele('提示')
    result_list = [result1, result2, result3, result4, result5]
    assert False not in result_list
    browser.cancel_sign_in(business='batch_sign_in', batch_name=text)


@allure.epic('健康管理系统')
@allure.feature('体检登记-项目与性别')
@allure.story('项目选定后更改性别提示')
def test_pe_registration_case31():
    browser = Registration('体检登记', 'peis', 'Chrome')
    browser.driver.continuous_clicks('年龄输入框：20|套餐搜索框：镇海联合发电(男)|套餐1|'
                                     '套餐-项目选择键|性别切换|性别女')
    result = browser.driver.exists_judge('输入提示', By.CSS_SELECTOR)
    assert result is True


if __name__ == '__main__':
    pytest.main(["-s", "-v"])
