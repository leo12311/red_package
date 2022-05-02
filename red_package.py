import uiautomator2 as u2#引用ui自动化库
import time
d = u2.connect()#连接好安卓设备
d.app_start("com.tencent.mm")#打开微信

def get_red_package():
    try:
        red_package = d(resourceId='com.tencent.mm:id/y4', text='微信红包')
        if red_package:
            # print('find read package')
            red_package[-1].click()
            time.sleep(0.05)
            open_button = d(resourceId="com.tencent.mm:id/giy")
            if open_button:  # 没抢过
                open_button.click()
                time.sleep(2)
                if d(resourceId="com.tencent.mm:id/gcq"):
                    print('已抢到红包金额：'+d(resourceId="com.tencent.mm:id/gcq").get_text()+'元')
                    d.press("back")
            elif d(resourceId='com.tencent.mm:id/giw', description='关闭'):  # 手慢了，红包被抢完了
                d(resourceId='com.tencent.mm:id/giw', description='关闭').click()
            elif d(resourceId="com.tencent.mm:id/gcq"):  # 已经抢过
                d.press("back")
    except BaseException:
        print("get_red_package 程序异常，重新执行")


#从所有未读消息中抢红包
def get_all_red_package():
    try:
        new_message = d(resourceId="com.tencent.mm:id/kn6")
        if not new_message:
            new_message = d(resourceId="com.tencent.mm:id/a2f")
        if new_message:
            new_message.click()
            for i in range(3):
                get_red_package()
            d.press("back")
            # pass
        else:
            # 判断是否在微信主页，否则重启微信
            if not d(resourceId="com.tencent.mm:id/f1c"):
                d.app_stop("com.tencent.mm")
                d.app_start("com.tencent.mm")
                time.sleep(5)
            # else:
            #     print('in main page')
                # d(resourceId="com.tencent.mm:id/l0n").click()
    except BaseException:
        print("get_all_red_package 程序异常，重新执行")

while True:
    get_all_red_package()
    # get_red_package()