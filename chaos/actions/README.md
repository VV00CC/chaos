# chaos
work with python + selenium + appium UI automation test tool

## SeleniumPage中常用API说明
### 所有元素寻找等待时长默认为10s, 可修改
1.	设置寻找元素时最长等待时间
Action.set_timeout(10)

输入参数：等待时长，单位秒

返回值：无


2.	打开页面
Action.open(url, pagetitle)
输入参数：要打开的url; 打开页面的head title
返回值：无
失败：打开url异常写入log，head title不匹配写入report

3.	匹配当前页面title是否为指定title
Action.on_page(pagetitle)
输入参数：页面的head title
返回值：True/False

4.	匹配当前页面内容是否包含指定值
Action.on_page_source(content)
输入参数：期望页面包含的内容
返回值：True/False

5.	点击元素
Action.click(loc,is_child=False,ploc=None,pEl=None)
输入参数：元素locator; 是否为子元素; 父元素locator; 父元素对象（后两个参数填一个即可，都填以父元素locator为准）
返回值：无
失败：找不到元素，则把异常信息写入report和log

6.	元素中输入文字
若找不到元素，则把异常信息写入report
Action.send_keys(loc, vaule, clear_first=True, click_first=True)
输入参数：元素locator; 要输入的文字; 写入之前是否清空输入框中的内容；输入之前是否先点击元素聚焦
返回值：无
失败：找不到元素，则把异常信息写入report和log

7.	获取元素属性
Action.get_attribute(loc,attr_name,is_child=False,pEl=None)
输入参数：元素locator; 属性名; 是否为子元素; 父元素对象
返回值：文本
失败：找不到元素，则把异常信息写入report和log，返回空文本

8.	获取元素的Text文字
Action.get_text(loc,is_child=False,pEl=None)
输入参数：元素locator; 是否为子元素; 父元素对象
返回值：文本
失败：找不到元素，则把异常信息写入log，返回空文本

9.	判断元素存在
Action .exist_element(loc)
输入参数：元素locator
返回值：True/None
失败：None

10.	获取元素个数
Action .get_elements_count(loc)
输入参数：元素locator
返回值：数字
失败：0


11.	查找元素集合
Action.find_elements(loc)
输入参数：元素locator
返回值：元素集合
失败：raise NoneWebElementErr，打印异常信息到log

12.	查找元素
Action.find_element(loc)
输入参数：元素locator
返回值：元素对象
失败：raise NoneWebElementErr，打印异常信息到log

13.	查找子元素
Action.find_child_element(el,loc)
输入参数：父元素对象，子元素locator
返回值：子元素对象
失败：raise NoneWebElementErr，打印异常信息到log

14.	查找enable的元素
Action.find_enable_element(loc)
输入参数：元素locator
返回值：元素对象
失败：raise NoneWebElementErr，打印异常信息到log


15.	查找enable的子元素
Action.find_enable_child_element(el,loc)
输入参数：父元素对象，子元素locator
返回值：子元素对象
失败：raise NoneWebElementErr，打印异常信息到log

16.	查找页面中存在的元素
Action.find_present_element(loc)
输入参数：元素locator
返回值：元素对象
失败：raise NoneWebElementErr，打印异常信息到log

17.	查找可点击的元素
Action.find_clickable_element(loc)
输入参数：元素locator
返回值：元素对象
失败：raise NoneWebElementErr，打印异常信息到log

18.	切换上下文
Action.switch_context(ctx_name)
输入参数：上下文名字
返回值：True/False
失败：返回False, 把异常信息写入report和log

19.	切换到默认上下文
Action.switch_default_context()
输入参数：无
返回值：同” switch_context”
失败：同” switch_context”

20.	切换frame
Action.switch_frame(loc)
输入参数：frame locator
返回值：frame对象
失败：写入异常信息到log

21.	执行js脚本
Action .script(src)
输入参数：js脚本
返回值：无

22.	点击手机返回键
Action .goback()
输入参数：无
返回值：无
23.	退出浏览器
Action .close()
输入参数：无
返回值：无


