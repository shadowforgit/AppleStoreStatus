from check_availability import check_availability
from wxpy_usage import WechatAlarm
import threading
from datetime import datetime

from store import get_sz_stores_number
from store import get_all_stores_number
import winsound


# wechat_alarm = WechatAlarm()

WANTED_MODEL = 'MGLD3CH/A'  # iphone 12 pro 海蓝色


class SpyderTimer:
    def __init__(self):
        self.check_stores = get_sz_stores_number()
        self.checkup_and_alarm()

    def checkup_and_alarm(self):
        res, yoho = check_availability(self.check_stores, WANTED_MODEL)
        print('='*60)
        print(datetime.now())
        if yoho:
            print('有货！已经微信发过去了')
            # wechat_alarm.send_msg(str(res))
            winsound.PlaySound('2.wav', winsound.SND_FILENAME)
            winsound.Beep(1000, 1000)  # 蜂鸣器报警
        else:
            print('没货！')
        global timer
        timer = threading.Timer(5.0, self.checkup_and_alarm)
        timer.start()


if __name__ == '__main__':
    SpyderTimer()
