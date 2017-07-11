# chaos
work with python + selenium + appium UI automation test tool

## 框架说明：
+ actions文件夹，主要用来封装要测试产品的页面，和产品中逻辑相关的action
  - SeleniumPage：
存放封装好的常用API，API说明可参见actions下的《readme》
  - example_page：
封装测试产品页面的示例
  - example_actions：
封装逻辑action的示例
  - init_driver：
封装初始化selenium和appium driver的参数
+ lib文件夹下存放本框架相关的文件
+ log文件夹下存放运行过程中打印的log文件
+ results文件夹下存放test case运行后产生的report
+ scripts文件夹下存放test case脚本
  - example：
封装test case的模板



## 使用步骤：
* 安装框架引入的Python模块
* 参照actions文件夹下的example_page，封装要测试产品的页面
* 参照actions文件夹下的example_ actions，封装测试产品业务逻辑的action
* 参照scripts文件夹下的example，封装test case
* 修改actions文件夹下的init_driver中的参数为测试设备的参数
* 双击scripts文件夹下test case的脚本执行test case
* results文件夹下查看test report
