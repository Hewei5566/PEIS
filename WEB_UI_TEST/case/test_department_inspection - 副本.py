import pytest
import allure
from WEB_UI_TEST.business_methods.department_inspection import DepartInspect
from selenium.webdriver.common.by import By


@allure.epic('健康管理系统')
@allure.feature('科室检查-体检人员列表')
@allure.story('时间搜索验证')
def test_department_inspection_case1():
    browser = DepartInspect('科室检查', 'peis', 'Chrome').driver
    browser.continuous_clicks('科室检查-开始日期|科室检查-开始日期向前一月|科室检查-开始具体日期|科室检查-搜索')
    result = browser.text_ele('科室检查-搜索结果')
    assert '没有搜索到相关体检人员' in browser.text_ele('提示') or len(result) != 0, '时间搜索验证,校验失败'


@allure.epic('健康管理系统')
@allure.feature('科室检查-体检人员列表')
@allure.story('时间范围错误搜索验证')
def test_department_inspection_case2():
    browser = DepartInspect('科室检查', 'peis', 'Chrome').driver
    browser.continuous_clicks('科室检查-结束日期|科室检查-结束日期向前一月|科室检查-结束具体日期|科室检查-搜索')
    assert '开始时间不可大于结束时间' in browser.text_ele('日期范围提示', By.CSS_SELECTOR), '时间范围错误搜索验证,校验失败'


@allure.epic('健康管理系统')
@allure.feature('科室检查-体检类型')
@allure.story('体检类型检查及功能确认')
def test_department_inspection_case3():
    browser = DepartInspect('科室检查', 'peis', 'Chrome')
    result = browser.type_check('科室检查-体检类型', '15')
    assert result is True, '体检类型检查及功能确认,校验失败'


@allure.epic('健康管理系统')
@allure.feature('科室检查-搜索类型')
@allure.story('默认搜索类型及切换')
def test_department_inspection_case4():
    browser = DepartInspect('科室检查', 'peis', 'Chrome').driver
    default_result = '单位' not in browser.text_recognition('搜索信息表')
    browser.continuous_clicks('搜索类型下拉按钮|高级搜索')
    change_result = '单位' in browser.text_recognition('搜索信息表')
    assert default_result is True and change_result is True, '默认搜索类型及切换,校验失败'


@allure.epic('健康管理系统')
@allure.feature('科室检查-高级搜索')
@allure.story('高级搜索-点击搜索')
def test_department_inspection_case5():
    browser = DepartInspect('科室检查', 'peis', 'Chrome').driver
    browser.continuous_clicks('搜索类型下拉按钮|高级搜索|团队批次下拉按钮|散客批次/css|科室检查-搜索')
    text = browser.text_ele('科室检查-搜索结果')
    result = '没有搜索到相关体检人员' in browser.text_ele('提示') or len(text) != 0
    assert result is True, '高级搜索-点击搜索,校验失败'


@allure.epic('健康管理系统')
@allure.feature('科室检查-高级搜索')
@allure.story('高级搜索-输入搜索')
def test_department_inspection_case6():
    browser = DepartInspect('科室检查', 'peis', 'Chrome').driver
    browser.continuous_clicks('搜索类型下拉按钮|高级搜索|团队批次下拉按钮|团队批次输入框：散客')
    result1 = '散客' in browser.text_recognition('团队批次搜索结果', By.CSS_SELECTOR)
    browser.continuous_clicks('团队批次搜索结果/css|科室检查-搜索')
    result2 = '没有搜索到相关体检人员' in browser.text_ele('提示') or len(browser.text_ele('科室检查-搜索结果')) != 0
    assert result1 is True and result2 is True, '高级搜索-输入搜索,校验失败'


@allure.epic('健康管理系统')
@allure.feature('科室检查-搜索')
@allure.story('姓名搜索')
def test_department_inspection_case7():
    browser = DepartInspect('科室检查', 'peis', 'Chrome').driver
    browser.continuous_clicks('科室检查-姓名输入框：奥特曼|科室检查-搜索')
    no_result = '没有搜索到相关体检人员' in browser.text_ele('提示')
    browser.continuous_clicks('科室检查-开始日期|科室检查-开始日期向前一月|科室检查-开始具体日期')
    browser.set_empty('科室检查-姓名输入框')
    browser.continuous_clicks('科室检查-姓名输入框：sxx|科室检查-搜索')
    yes_result = len(browser.text_ele('科室检查-搜索结果')) != 0
    assert yes_result is True and no_result is True


@allure.epic('健康管理系统')
@allure.feature('科室检查-搜索')
@allure.story('搜索条件重置')
def test_department_inspection_case8():
    browser = DepartInspect('科室检查', 'peis', 'Chrome')
    browser.driver.continuous_clicks('搜索类型下拉按钮|高级搜索')
    browser.continuous_input('科室检查-姓名输入框', '迪迦', '科室检查-编号输入框', '奥特军团007',
                             '科室检查-住址输入框', 'M78星云')
    input_result = '迪迦' and 'M78星云' and '奥特军团' in browser.driver.text_recognition('搜索信息表')
    browser.driver.click_ele('科室检查-搜索重置')
    reset_result = '迪迦' and 'M78星云' and '奥特军团' not in browser.driver.text_recognition('搜索信息表')
    assert input_result is True and reset_result is True, '搜索条件重置，校验失败'


@allure.epic('健康管理系统')
@allure.feature('科室检查-搜索')
@allure.story('当周搜')
def test_department_inspection_case9():
    browser = DepartInspect('科室检查', 'peis', 'Chrome')
    # now_time = time.strftime("%Y-%m-%d", time.localtime())
    # default_result = now_time in browser.text_recognition('开始日期信息栏')
    # browser.continuous_clicks('搜索类型下拉按钮|一周体检人员|科室检查-搜索')
    # week_ago = (datetime.datetime.now() - relativedelta(weeks=1)).strftime("%Y-%m-%d")
    # change_result = week_ago in browser.text_recognition('开始日期信息栏')
    # search_result = len(browser.text_ele('科室检查-搜索结果')) != 0 or '没有搜索到相关人员' in browser.text_ele('提示')
    result_list = browser.week_search()
    assert False not in result_list, '当周搜,校验失败'


@allure.epic('健康管理系统')
@allure.feature('科室检查-搜索')
@allure.story('当月搜')
def test_department_inspection_case10():
    browser = DepartInspect('科室检查', 'peis', 'Chrome')
    result_list = browser.month_search()
    assert False not in result_list, '当月搜,校验失败'


@allure.epic('健康管理系统')
@allure.feature('科室检查-未检已检')
@allure.story('未检已检切换')
def test_department_inspection_case11():
    browser = DepartInspect('科室检查', 'peis', 'Chrome')
    result_list = browser.check_state()
    assert False not in result_list, '未检已检切换，校验失败'


@allure.epic('健康管理系统')
@allure.feature('科室检查-手动输入卡号')
@allure.story('手动输入卡号')
def test_department_inspection_case12():
    browser = DepartInspect('科室检查', 'peis', 'Chrome').driver
    browser.continuous_clicks('科室检查-开始日期|科室检查-开始日期向前一月|科室检查-开始具体日期|科室检查-搜索')
    number = browser.text_ele('科室检查-搜索结果2编号', By.CSS_SELECTOR)
    browser.continuous_clicks(f'体检人员列表-编号输入框：{number}|体检人员列表-编号输入框：ENTER|提示确定/css')
    assert browser.text_ele('科室检查-搜索结果1编号', By.CSS_SELECTOR) == number, '手动输入卡号，校验失败'


# @allure.epic('健康管理系统')
# @allure.feature('科室检查-手动输入身份证')
# @allure.story('手动输入身份证')
# def test_department_inspection_case13():
#     browser = DepartInspect('科室检查', 'peis', 'Chrome').driver
#     browser.continuous_clicks('科室检查-开始日期|科室检查-开始日期向前一月|科室检查-开始具体日期|科室检查-搜索')
#     number = browser.text_ele('科室检查-搜索结果2身份证', By.CSS_SELECTOR)
#     browser.input_ele('体检人员列表-编号输入框', number)
#     browser.ele_location(locate_value='体检人员列表-编号输入框').send_keys(Keys.ENTER)
#     browser.continuous_clicks('提示确定|科室检查-取消|提示确定', By.CSS_SELECTOR)
#     assert browser.text_ele('科室检查-搜索结果1身份证', By.CSS_SELECTOR) == number, '手动输入身份证，校验失败'


@allure.epic('健康管理系统')
@allure.feature('科室检查-记录')
@allure.story('用户未付费')
def test_department_inspection_case14():
    browser = DepartInspect('科室检查', 'peis', 'Chrome').driver
    browser.continuous_clicks('体检人员列表-编号输入框：202105274279111|体检人员列表-编号输入框：ENTER')
    browser.exists_judge('提示确定', By.CSS_SELECTOR)
    assert '未收费，不允许进行科室检查' in browser.text_ele('提示'), '用户未付费，校验失败'


@allure.epic('健康管理系统')
@allure.feature('科室检查-记录')
@allure.story('团队用户已付费')
def test_department_inspection_case15():
    browser = DepartInspect('科室检查', 'peis', 'Chrome').driver
    browser.continuous_clicks('体检人员列表-编号输入框：202105281304|体检人员列表-编号输入框：ENTER')
    result = browser.exists_judge('提示确定', By.CSS_SELECTOR)
    assert result is True, '团队用户已付费，校验失败'


@allure.epic('健康管理系统')
@allure.feature('科室检查-记录')
@allure.story('个人用户已付费')
def test_department_inspection_case16():
    browser = DepartInspect('科室检查', 'peis', 'Chrome').driver
    browser.continuous_clicks('体检人员列表-编号输入框：202105281135|体检人员列表-编号输入框：ENTER')
    result = browser.exists_judge('提示确定', By.CSS_SELECTOR)
    assert result is True, '个人用户已付费，校验失败'


@allure.epic('健康管理系统')
@allure.feature('科室检查-记录')
@allure.story('指标模板替换保存')
def test_department_inspection_case17():
    browser = DepartInspect('科室检查', 'peis', 'Chrome')
    result_list = browser.checked_result_save('模板输入')
    assert False not in result_list, '指标模板替换保存，校验失败'


@allure.epic('健康管理系统')
@allure.feature('科室检查-记录')
@allure.story('指标输入保存')
def test_department_inspection_case18():
    browser = DepartInspect('科室检查', 'peis', 'Chrome')
    result_list = browser.checked_result_save('键盘输入', '5')
    assert False not in result_list, '指标输入保存，校验失败'


@allure.epic('健康管理系统')
@allure.feature('科室检查-记录')
@allure.story('指标输入取消')
def test_department_inspection_case19():
    browser = DepartInspect('科室检查', 'peis', 'Chrome')
    browser.account_check()
    browser.driver.continuous_clicks('体检人员列表-编号输入框：202105281305|体检人员列表-编号输入框：ENTER|提示确定/css|科室检查-指标框1')
    browser.driver.input_ele('科室检查-结果输入框', '10', By.CSS_SELECTOR)
    result = '10' in browser.driver.text_recognition('科室检查-指标框1')
    browser.driver.set_empty('科室检查-结果输入框', By.CSS_SELECTOR)
    browser.driver.click_ele('科室检查-保存')
    assert result is True and '保存失败' in browser.driver.text_ele('提示'), '指标输入取消，校验失败'


@allure.epic('健康管理系统')
@allure.feature('科室检查-记录')
@allure.story('多指标输入')
def test_department_inspection_case20():
    browser = DepartInspect('科室检查', 'peis', 'Chrome')
    result_list = browser.checked_result_save('模板输入', number=5)
    assert False not in result_list


@allure.epic('健康管理系统')
@allure.feature('科室检查-记录')
@allure.story('默认结果保存')
def test_department_inspection_case21():
    browser = DepartInspect('科室检查', 'peis', 'Chrome')
    result_list = browser.checked_result_save('默认结果')
    assert False not in result_list, '默认结果保存，校验失败'


@allure.epic('健康管理系统')
@allure.feature('科室检查-记录')
@allure.story('先输入后默认结果保存')
def test_department_inspection_case22():
    browser = DepartInspect('科室检查', 'peis', 'Chrome')
    result_list = browser.checked_result_save('先输入后默认', '100')
    assert False not in result_list, '先输入后默认结果保存，校验失败'


@allure.epic('健康管理系统')
@allure.feature('科室检查-记录')
@allure.story('先默认后修改结果保存')
def test_department_inspection_case23():
    browser = DepartInspect('科室检查', 'peis', 'Chrome')
    result_list = browser.checked_result_save('先默认后修改', '100')
    assert False not in result_list, '先默认后修改结果保存，校验失败'


@allure.epic('健康管理系统')
@allure.feature('科室检查-记录')
@allure.story('指标异常保存')
def test_department_inspection_case24():
    browser = DepartInspect('科室检查', 'peis', 'Chrome')
    browser.account_check()
    browser.driver.continuous_clicks('体检人员列表-编号输入框：202105281305|体检人员列表-编号输入框：ENTER|'
                                     '提示确定/css|科室检查-指标框2|指标结果模板替换/css|科室检查-指标框1')
    result1 = '↑' in browser.driver.text_ele('标记信息栏')
    browser.driver.continuous_clicks('科室检查-保存|科室检查-已检|体检人员列表-编号输入框：ENTER')
    result2 = '↑' in browser.driver.text_recognition('科室检查-科室小结信息栏')
    browser.driver.continuous_clicks('科室检查-取消检查|提示确定/css')
    assert result1 is True and result2 is True, '指标异常保存，校验失败'


@allure.epic('健康管理系统')
@allure.feature('科室检查-记录')
@allure.story('输入科室小结保存')
def test_department_inspection_case25():
    browser = DepartInspect('科室检查', 'peis', 'Chrome')
    browser.account_check()
    browser.driver.continuous_clicks('体检人员列表-编号输入框：202105281305|体检人员列表-编号输入框：ENTER|提示确定/css|'
                                     '科室检查-指标框2|指标结果模板替换/css|科室检查-指标框1|科室检查-科室小结信息栏：存在异常指标|'
                                     '科室检查-保存|提示取消/css|科室检查-已检|体检人员列表-编号输入框：ENTER')
    browser.save_check()
    assert '存在异常指标' in browser.driver.text_recognition('科室检查-科室小结信息栏'), '指标异常保存，校验失败'


@allure.epic('健康管理系统')
@allure.feature('科室检查-记录')
@allure.story('生成科室小结')
def test_department_inspection_case26():
    browser = DepartInspect('科室检查', 'peis', 'Chrome')
    browser.account_check()
    browser.driver.continuous_clicks('体检人员列表-编号输入框：202105281305|体检人员列表-编号输入框：ENTER|'
                                     '提示确定/css|科室检查-默认结果|科室检查-保存|体检人员列表-编号输入框：ENTER')
    result_list = browser.save_check()
    result_list.append('未见异常' in browser.driver.text_recognition('科室检查-科室小结信息栏'))
    assert False not in result_list, '生成科室小结，校验失败'


@allure.epic('健康管理系统')
@allure.feature('科室检查-记录')
@allure.story('输入科室小结后重新生成覆盖保存')
def test_department_inspection_case27():
    browser = DepartInspect('科室检查', 'peis', 'Chrome')
    browser.account_check()
    browser.driver.continuous_clicks('体检人员列表-编号输入框：202105281305|体检人员列表-编号输入框：ENTER|提示确定/css|'
                                     '科室检查-指标框2|指标结果模板替换/css|科室检查-指标框1|科室检查-科室小结信息栏：存在异常指标|'
                                     '科室检查-保存|提示确定/css|科室检查-已检|体检人员列表-编号输入框：ENTER')
    browser.save_check()
    assert '↑' in browser.driver.text_recognition('科室检查-科室小结信息栏'), '指标异常保存，校验失败'


@allure.epic('健康管理系统')
@allure.feature('科室检查-记录')
@allure.story('科室小结与诊断切换')
def test_department_inspection_case28():
    browser = DepartInspect('科室检查', 'peis', 'Chrome')
    browser.account_check()
    browser.driver.continuous_clicks('体检人员列表-编号输入框：202105281305|体检人员列表-编号输入框：ENTER')
    default_result = '生成小结' in browser.driver.text_ele('科室检查-科室小结选项栏')
    browser.driver.continuous_clicks('提示确定/css|科室检查-诊断')
    change_result = '默认诊断' in browser.driver.text_ele('科室检查-诊断选项栏')
    assert default_result is True and change_result is True, '科室小结与诊断切换，校验失败'


@allure.epic('健康管理系统')
@allure.feature('科室检查-记录')
@allure.story('新增一条诊断')
def test_department_inspection_case29():
    browser = DepartInspect('科室检查', 'peis', 'Chrome')
    browser.enter_diagnosis_sheet()
    browser.add_diagnosis('1')
    text = browser.driver.text_ele('科室检查-诊断信息')
    browser.driver.continuous_clicks('科室检查-保存|体检人员列表-编号输入框：ENTER|科室检查-诊断')
    assert browser.driver.text_ele('科室检查-诊断信息') in text
    browser.delete_diagnosis('1')

'30 32 40 41 42'
@allure.epic('健康管理系统')
@allure.feature('科室检查-记录')
@allure.story('新增多条诊断')
def test_department_inspection_case30():
    browser = DepartInspect('科室检查', 'peis', 'Chrome')
    browser.enter_diagnosis_sheet()
    browser.add_diagnosis('3')
    browser.driver.continuous_clicks('科室检查-保存|体检人员列表-编号输入框：ENTER|提示确定/css|科室检查-诊断')
    assert len(browser.driver.text_ele('科室检查-诊断信息')) > 20
    browser.delete_diagnosis('3')


@allure.epic('健康管理系统')
@allure.feature('科室检查-记录')
@allure.story('新增后取消')
def test_department_inspection_case31():
    browser = DepartInspect('科室检查', 'peis', 'Chrome')
    browser.enter_diagnosis_sheet()
    browser.add_diagnosis('1')
    result1 = len(browser.driver.text_ele('科室检查-诊断信息')) > 10
    browser.driver.continuous_clicks('科室检查-取消|提示确定/css|体检人员列表-编号输入框：ENTER|提示确定/css|科室检查-诊断')
    result2 = len(browser.driver.text_ele('科室检查-诊断信息')) == 0
    assert result1 is True and result2 is True


@allure.epic('健康管理系统')
@allure.feature('科室检查-记录')
@allure.story('新增搜索保存')
def test_department_inspection_case32():
    browser = DepartInspect('科室检查', 'peis', 'Chrome')
    browser.enter_diagnosis_sheet('诊断新增', '诊断模板搜索框：中耳炎')
    result1 = '中耳炎' in browser.driver.text_ele('科室检查-诊断模板1')
    browser.driver.continuous_clicks('科室检查-诊断模板1|科室检查-指标框2')
    result2 = '中耳炎' in browser.driver.text_ele('科室检查-诊断信息')
    browser.driver.continuous_clicks('科室检查-保存')
    assert result1 is True and result2 is True
    browser.delete_diagnosis('1')


@allure.epic('健康管理系统')
@allure.feature('科室检查-记录')
@allure.story('诊断新增页面展示')
def test_department_inspection_case33():
    browser = DepartInspect('科室检查', 'peis', 'Chrome')
    browser.enter_diagnosis_sheet('诊断新增', '诊断模板默认展示数')
    text1 = browser.driver.text_ele('科室检查-诊断模板信息')
    browser.driver.continuous_clicks('科室检查-诊断模板展示数2|科室检查-诊断模板页数输入框：01|科室检查-诊断模板页数输入框：ENTER')
    result1 = text1 != browser.driver.text_ele('科室检查-诊断模板信息')
    text2 = browser.driver.text_recognition('科室检查-诊断模板底部信息栏')
    result2 = '显示2001到2020' in text2 and '101' in text2
    result3 = browser.page_change()
    result_list = [result1, result2]
    assert False not in result_list and False not in result3


@allure.epic('健康管理系统')
@allure.feature('科室检查-记录')
@allure.story('诊断增加描述')
def test_department_inspection_case34():
    browser = DepartInspect('科室检查', 'peis', 'Chrome')
    browser.enter_diagnosis_sheet('诊断新增', '诊断模板1')
    browser.input_diagnostic_info('诊断描述1', '诊断描述输入框', '一个不太严重的病', By.CSS_SELECTOR)
    browser.input_diagnostic_info('诊断处理意见1', '诊断处理意见输入框', '好好休息就行', By.CSS_SELECTOR)
    input_result = browser.driver.text_recognition('科室检查-诊断信息')
    assert '一个不太严重的病' in input_result and '好好休息就行' in input_result


@allure.epic('健康管理系统')
@allure.feature('科室检查-记录')
@allure.story('删除诊断')
def test_department_inspection_case35():
    browser = DepartInspect('科室检查', 'peis', 'Chrome')
    browser.enter_diagnosis_sheet()
    browser.add_diagnosis('1')
    result1 = len(browser.driver.text_recognition('科室检查-诊断信息')) > 10
    browser.driver.continuous_clicks('科室检查-诊断删除|提示确定/css')
    result2 = len(browser.driver.text_recognition('科室检查-诊断信息')) == 0
    assert result1 is True and result2 is True


@allure.epic('健康管理系统')
@allure.feature('科室检查-记录')
@allure.story('诊断向上、向下')
def test_department_inspection_case36():
    browser = DepartInspect('科室检查', 'peis', 'Chrome')
    browser.enter_diagnosis_sheet()
    browser.add_diagnosis('2')
    text1 = browser.driver.text_ele('科室检查-诊断信息')
    browser.driver.click_ele('科室检查-诊断向上')
    result1 = text1 != browser.driver.text_ele('科室检查-诊断信息')
    browser.driver.click_ele('科室检查-诊断向下')
    result2 = text1 == browser.driver.text_ele('科室检查-诊断信息')
    assert result1 is True and result2 is True


@allure.epic('健康管理系统')
@allure.feature('科室检查-记录')
@allure.story('生成诊断')
def test_department_inspection_case37():
    browser = DepartInspect('科室检查', 'peis', 'Chrome')
    browser.enter_diagnosis_sheet('生成诊断')
    assert '血压偏高' in browser.driver.text_ele('科室检查-诊断信息')


@allure.epic('健康管理系统')
@allure.feature('科室检查-检查科室')
@allure.story('检查科室选择')
def test_department_inspection_case38():
    browser = DepartInspect('科室检查', 'peis', 'Chrome').driver
    browser.continuous_clicks('科室检查-开始日期|科室检查-开始日期向前一月|科室检查-开始具体日期|科室检查-搜索')
    result = browser.text_ele('科室检查-搜索结果')
    browser.continuous_clicks('科室检查-科室下拉按钮|科室检查-科室2')
    assert result != browser.text_ele('科室检查-搜索结果')


@allure.epic('健康管理系统')
@allure.feature('科室检查-检查科室')
@allure.story('检查科室选择')
def test_department_inspection_case39():
    browser = DepartInspect('科室检查', 'peis', 'Chrome')
    browser.account_check()
    browser.driver.continuous_clicks('体检人员列表-编号输入框：202105281305|体检人员列表-编号输入框：ENTER|提示确定/css')
    result = browser.driver.text_ele('科室检查-搜索结果')
    for info in result:
        assert info in browser.driver.text_ele('科室检查-个人信息栏')


@allure.epic('健康管理系统')
@allure.feature('科室检查-记录')
@allure.story('诊断撤销')
def test_department_inspection_case40():
    browser = DepartInspect('科室检查', 'peis', 'Chrome')
    browser.enter_diagnosis_sheet('保存', '体检人员列表-编号输入框：ENTER', '记录', '提示确定/css', '诊断', '诊断新增',
                                  '诊断模板1')
    result1 = len(browser.driver.text_recognition('科室检查-诊断信息')) > 10
    browser.driver.continuous_clicks('科室检查-撤销|提示确定/css')
    result2 = len(browser.driver.text_recognition('科室检查-诊断信息')) == 0 and browser.driver.text_recognition(
        '科室检查-指标框2') == '333'
    assert result1 is True and result2 is True
    browser.driver.continuous_clicks('科室检查-保存|提示确定/css|体检人员列表-编号输入框：ENTER|科室检查-取消检查|提示确定/css')


@allure.epic('健康管理系统')
@allure.feature('科室检查-弃检')
@allure.story('弃检验证')
def test_department_inspection_case41():
    browser = DepartInspect('科室检查', 'peis', 'Chrome')
    result_list = browser.abandon_check()
    assert False not in result_list, '弃检验证，校验成功'


@allure.epic('健康管理系统')
@allure.feature('科室检查-弃检')
@allure.story('取消检查验证')
def test_department_inspection_case42():
    browser = DepartInspect('科室检查', 'peis', 'Chrome').driver
    browser.continuous_clicks('体检人员列表-编号输入框：202105281325|体检人员列表-编号输入框：ENTER|科室检查-取消检查|提示确定/css')
    assert '取消失败：没有需要取消检查的项目' in browser.text_ele('提示'), '取消检查验证，校验成功'


if __name__ == '__main__':
    pytest.main(["-s", "-v", "--alluredir"])
