# -*- coding: utf-8 -*-
# @Time    : 2024/3/14 1:52 下午
# @Author  : Hoey
import requests
from bs4 import BeautifulSoup

from util.common import not_in_list2
from util.file_utils import read_temp_file, append2_temp_file
from core.settings import Settings
from util.tg_notify_utils import send_message_to_notify_group

DEFAULT_PARSER = 'html.parser'


def get_pt_tieba_all_msg():
    """
    读取PT贴吧所有的数据
    :return:
    """
    response = requests.get(Settings.TIEBA_URL)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, DEFAULT_PARSER)
        posts = soup.find_all('div', class_='threadlist_lz clearfix')
        l_list = []
        for post in posts:
            title = post.find('a', class_='j_th_tit').get_text().replace("\n", ", ")
            l_list.append(title)

        return l_list


def filter_fayao_msg(keyword=Settings.TIEBA_FILTER_KEY):
    """
    过滤出发邀消息
    :param keyword:
    :return:
    """
    l_list = get_pt_tieba_all_msg()
    fayao_list = []
    for x in l_list:
        if x.find(keyword) != -1:
            fayao_list.append(x)
    fayao_list.sort()
    return fayao_list


def __send2tg(l_list):
    content = '**********************PT吧消息统计推送**********************'
    for msg in l_list:
        if msg.find(Settings.TIEBA_FILTER_KEY) != -1:
            content = content + msg + '\n'
    send_message_to_notify_group(Settings.MY_NOTIFY_CHAT_ID, content)


if __name__ == '__main__':
    fayao_list = filter_fayao_msg()
    # 读取temp_file中的list
    temp_file_list = read_temp_file(Settings.TEMP_TIEBA_MSG_FILE)
    # 在集合1不在集合2的title
    result_list = not_in_list2(fayao_list, temp_file_list)
    if len(result_list) != 0:
        # 将集合
        append2_temp_file(Settings.TEMP_TIEBA_MSG_FILE, result_list)
        __send2tg(result_list)
