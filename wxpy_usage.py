from wxpy import *


class WechatAlarm:
    def __init__(self, contact_name='Tecsun'):
        self.bot = Bot()
        self.my_friend = self.bot.friends().search(contact_name)[0]

    def send_msg(self, msg):
        self.my_friend.send(msg)


if __name__ == '__main__':
    wa = WechatAlarm()
    wa.send_msg('wxpy test!')

