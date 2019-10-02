from check_availability import check_availability
from wxpy_usage import WechatAlarm
import threading
from datetime import datetime


wechat_alarm = WechatAlarm()


class SpyderTimer:
    def __init__(self):
        self.checkup_and_alarm()

    def checkup_and_alarm(self):
        res, yoho = check_availability()
        print('='*60)
        print(datetime.now())
        if yoho:
            print('有货！已经微信发过去了')
            wechat_alarm.send_msg(str(res))
        else:
            print('没货！')
        global timer
        timer = threading.Timer(5.0, self.checkup_and_alarm)
        timer.start()


if __name__ == '__main__':
    SpyderTimer()
