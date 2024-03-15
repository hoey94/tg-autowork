# -*- coding: utf-8 -*-
# @Time    : 2024/3/14 1:46 下午
# @Author  : Hoey
import requests

from core.settings import Settings


def send_message_to_notify_group(chat_id, message):
    """
    发送消息到TG消息通知群
    :param message:
    :return:
    """
    notify_bot_url = f'https://api.telegram.org/bot{Settings.MY_NOTIFY_BOT_TOKEN}/sendMessage'
    params = {"chat_id": chat_id, "text": message}
    response = requests.get(notify_bot_url, params=params)

    if response.status_code == 200:
        print("Message sent successfully")
        return True
    else:
        print("Failed to send message")
        return False

