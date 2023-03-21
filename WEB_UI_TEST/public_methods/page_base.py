import os
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from WEB_UI_TEST.public_methods.same_use import pic_save, ocr


class BaseMethods(object):
    # 构造方法
    def __init__(self, browser, xpath_dict):
        """初始化浏览器对象"""
        # 根据传入的参数创建对应的浏览器对象（相关浏览器已正确安装驱动）
        if browser == 'EDGE':
            # 创建浏览器
            self.driver = webdriver.Edge()
        elif browser == 'Chrome':
            self.driver = webdriver.Chrome()
        # 默认最大化
        self.driver.maximize_window()
        self.xpath_dict = xpath_dict

    # 访问地址
    def open_url(self, url):
        # 访问url
        self.driver.get(url)
        # 默认隐式等待10
        self.driver.implicitly_wait(10)

    def ele_location(self, locate_type=None, locate_value=None):
        """
        定位元素，默认采用xpath定位

        ：使用方式（定位方式有默认值，可不填，根据实际情况选填）
            ①ele_location(locate_value = 定位值)

            ②ele_location(locate_type = 定位方式,locate_value = 定位值)

        :参数 locate_type:定位方式

        :参数 locate_value:定位值
        """
        # selenium可通过id、class_name、css_selector、xpath等8种定位方式，默认采用xpath定位
        if locate_type is None:
            locate_type = By.XPATH
        else:
            locate_type = locate_type
            # locate_type = f'By.{locate_type}'
        # 设置定位器条件，定位条件和定位值为传进来的参数locate_type, locate_value
        ele_id = self.xpath_dict[locate_value]
        locator = (locate_type, ele_id)
        # 等待元素出现，若5s内未出现，则报出错误
        WebDriverWait(self.driver, 5, 0.2).until(EC.visibility_of_element_located(locator),
                                                 f'5s内未定位到{ele_id}，超时')
        ele = self.driver.find_element(by=locate_type, value=ele_id)
        # 如果ele不为None,则返回
        if ele is not None:
            return ele

    def wait_disappear(self, wait_value, locate_type=None):
        ele_id = self.xpath_dict[wait_value]
        locator = (locate_type, ele_id)
        WebDriverWait(self.driver, 5, 0.2).until_not(EC.visibility_of_element_located(locator),
                                                     f'5s内{wait_value}未消失')

    # 指定某一个元素进行点击操作
    def click_ele(self, locate_value, locate_type=None):
        # 调用定位方法，定位指定的元素
        ele = self.ele_location(locate_value=locate_value, locate_type=locate_type)
        # 点击操作
        ele.click()
        time.sleep(1)
        if locate_value == '签到' or locate_value == '体检登记-保存':
            time.sleep(3)

    def continuous_double_clicks(self, click_value, locate_type=None):
        """
        连续双击，通过‘|’符号进行分割
        :param click_value:
        :param locate_type:
        :return:
        """
        ele_list = click_value.split('|')
        for element in ele_list:
            self.double_click(element, locate_type=locate_type)
            time.sleep(1)

    # 连续点击操作
    def continuous_clicks(self, click_value, locate_type=None):
        """
        连续单击及文本输入
        :param click_value: 要点击的元素通过'|'符号进行分割，如果是输入框或搜索框，可进行输入。用法举例：名字输入框：张三。（输入位置和输入内容通过‘_’符号连接）
        :param locate_type: 定位元素方式
        :return:
        """
        ele_list = click_value.split('|')
        for element in ele_list:
            if 'ENTER' in element:
                input_list = element.split('：')
                locate_type = None
                self.ele_location(locate_type=locate_type, locate_value=input_list[0]).send_keys(Keys.ENTER)
            else:
                if element == '无人批次':
                    time.sleep(3)
                if '/' in element:
                    type_list = element.split('/')
                    if type_list[1] == 'css':
                        locate_type = By.CSS_SELECTOR
                    else:
                        locate_type = type_list[1]
                    element = type_list[0]
                else:
                    element = element
                    locate_type = None
                if '：' in element:
                    input_list = element.split('：')
                    if input_list[0] == '单位输入框':
                        self.set_empty('单位输入框')
                    self.input_ele(input_list[0], input_list[1])
                    element = input_list[0]
                try:
                    self.click_ele(element, locate_type=locate_type)
                except:
                    pass

    # # 连续点击操作
    # def continuous_clicks(self, click_value, locate_type=None):
    #     """
    #     连续单击及文本输入
    #     :param click_value: 要点击的元素通过'|'符号进行分割，如果是输入框或搜索框，可进行输入。用法举例：名字输入框：张三。（输入位置和输入内容通过‘_’符号连接）
    #     :param locate_type: 定位元素方式
    #     :return:
    #     """
    #     ele_list = click_value.split('|')
    #     for element in ele_list:
    #         if element == '无人批次':
    #             time.sleep(3)
    #         if '/' in element:
    #             type_list = element.split('/')
    #             if type_list[1] == 'css':
    #                 locate_type = By.CSS_SELECTOR
    #             else:
    #                 locate_type = type_list[1]
    #             element = type_list[0]
    #         else:
    #             locate_type = None
    #         if '：' in element:
    #             input_list = element.split('：')
    #             if input_list[0] == '单位输入框':
    #                 self.ele_location(locate_value=input_list[0]).send_keys(Keys.BACKSPACE)
    #             if input_list[1] == 'ENTER':
    #                 self.ele_location(locate_type=locate_type, locate_value=input_list[0]).send_keys(Keys.ENTER)
    #             else:
    #                 self.input_ele(input_list[0], input_list[1])
    #             element = input_list[0]
    #         try:
    #             self.click_ele(element, locate_type=locate_type)
    #         except KeyError:
    #             pass

    # 指定元素进行输入
    def input_ele(self, locate_value, input_value, locate_type=None):
        # 调用定位方法，指定元素进行定位
        ele = self.ele_location(locate_value=locate_value, locate_type=locate_type)
        # 输入操作
        ele.send_keys(input_value)
        time.sleep(1)

    # 获取指定元素的文本内容
    def text_ele(self, locate_value, locate_type=None):
        # 调用定位方法定位指定元素
        ele = self.ele_location(locate_value=locate_value, locate_type=locate_type)
        # 获取文本内容
        return ele.text

    # 判断元素是否可见
    def ele_visual(self, locate_value, locate_type=None):
        try:
            self.ele_location(locate_value=locate_value, locate_type=locate_type)
            visual_result = True
        except KeyError:
            visual_result = False
        return visual_result

    # 关闭本脚本打开的窗口
    def close_browser(self):
        self.driver.quit()

    # 切换iframe
    def switch_iframe(self):
        iframe = self.driver.find_element(by=By.TAG_NAME, value='iframe')
        self.driver.switch_to.frame(iframe)

    # 双击操作
    def double_click(self, locate_value, locate_type=None):
        """
        双击操作
        """
        ActionChains(self.driver).double_click(
            self.ele_location(locate_value=locate_value, locate_type=locate_type)).perform()

    def set_empty(self, locate_value, locate_type=None):
        """
        输入框置空
        """
        self.double_click(locate_value=locate_value, locate_type=locate_type)
        for times in range(4):
            self.ele_location(locate_value=locate_value, locate_type=locate_type).send_keys(Keys.BACKSPACE)

    def text_recognition(self, locate_value, locate_type=None):
        """
        截图，截取指定控件，并返回文字识别的值
        """
        pic = pic_save()
        self.ele_location(locate_value=locate_value, locate_type=locate_type).screenshot(pic)
        result = ocr(pic)
        os.remove(pic)
        return result

    def screenshot(self, locate_value, locate_type=None):
        """
        截图，截取指定控件，并返回文字识别的值
        """
        pic = pic_save()
        self.ele_location(locate_value=locate_value, locate_type=locate_type).screenshot(pic)
        result = ocr(pic)
        os.remove(pic)
        return result

    def mouse_hover(self, locate_value):
        """
        鼠标悬停
        """
        ActionChains(self.driver).move_to_element(self.ele_location(locate_value=locate_value)).perform()

    def exists_judge(self, locate_value, locate_type=None):
        """
        判断元素是否存在
        """
        flag = True
        try:
            self.ele_location(locate_value=locate_value, locate_type=locate_type)
            return flag
        except:
            flag = False
            return flag
