# red_package- 微信抢红包
wechat red package tools -微信抢红包


# 功能描述
1.循环打开所有未读消息
2.查找未读消息是否有红包
3.点击某条未读信息（群或个人），连续查找三次是否存在红包，并且抢红包，之后返回微信主界面
4.判断是否成功返回主界面，否则重启微信进入微信主界面

# 前置条件
1.安装python
2.安装uiautomator2

# 遗留问题
由于不能识别是否已经点击过该红包，（可以考虑后续使用opencv基于图像识别优化），目前只抢聊天窗口的最新的一个红包
