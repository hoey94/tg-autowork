# -*- coding: utf-8 -*-
# @Time    : 2024/3/14 2:35 下午
# @Author  : Hoey

from datetime import datetime, timedelta

from core.settings import Settings
from util.simple_cache import SimpleCache
from util.tg_notify_utils import send_message_to_notify_group
from util.tg_scrapper_utils import tlg_connect, tlg_get_basic_info, tlg_get_messages


def _check(msg_content, filter_list):
    for kw in filter_list:
        if kw in msg_content:
            return True
        else:
            return False

    return False


def save_cache(chat_link, messages):
    """
    将最新的消息偏移量存储到缓存
    :param chat_link:
    :param messages:
    :return:
    """
    if len(messages) != 0:
        cache = SimpleCache()
        cache.put(chat_link, messages[0].get('id'))


def date_change(datetime_str):
    # 将原始时间字符串转换为datetime对象
    original_time = datetime.strptime(datetime_str, "%d/%m/%Y %H:%M:%S")
    # 加上8个小时
    adjusted_time = original_time + timedelta(hours=8)
    # 将调整后的时间转换为指定格式的字符串
    adjusted_time_str = adjusted_time.strftime("%Y-%m-%d %H:%M:%S")
    return adjusted_time_str


def filter_and_get_content(chat_link, messages):
    """
    过滤消息并且重新整理格式
    :param messages:
    :return:
    """
    filter_list = Settings.TG_MSG_FILTER_LIST
    print(f'{chat_link}获取到的信息消息共{len(messages)}条')
    print(f'过滤规则为: {",".join(filter_list)}')
    reslut_list = []
    for msg in messages:
        msg_content = msg.get('text')
        msg_sent_date = msg.get('sent_date')
        msg_sent_time = msg.get('sent_time')
        d_datetime = date_change(f'{msg_sent_date} {msg_sent_time}')
        if _check(msg_content, filter_list):
            reslut_list.append(f'{d_datetime} {msg_content}')
    print(f'{chat_link}过滤后的信息消息共{len(reslut_list)}条')
    return reslut_list


def get_notify_msg(tg_client, chat_link, msg_num, last_max_offset_id=None):
    print(f'*******************开始处理chat_link: {chat_link}*******************')
    notify_msg = None
    if tg_client is not None:
        # Get chat basic info
        print('开始获取群组基础信息...')
        chat_info = tlg_get_basic_info(tg_client, chat_link)
        group_name = chat_info['title']
        print(f'获取【{group_name}】群组基础成功...')
        # 获取消息
        print(f'开始获取群组聊天信息，从消息偏移{last_max_offset_id}开始，待拉取{msg_num}条记录...')
        messages = tlg_get_messages(tg_client, chat_link, msg_num, offset_id=last_max_offset_id)
        save_cache(chat_link, messages)
        # 过滤并整理新的格式
        reslut_list = filter_and_get_content(chat_link, messages)
        if len(reslut_list) == 0:
            print(f"【{group_name}】 检查完毕，没有发现发药信息")
            return None
        else:
            print(f"在群组【{group_name}】中检查到发药信息，开始推送TG...")
            result_content = '\n'.join(reslut_list)
            notify_msg = f"******TG监控: {group_name}******* \n{result_content}"

    return notify_msg


if __name__ == "__main__":
    cache = SimpleCache()
    chat_links = Settings.CHAT_LINKS
    client = tlg_connect(Settings.API_ID, Settings.API_HASH, Settings.PHONE_NUM)
    notify_msg_list = []

    for chat_link in chat_links:
        notify_msg = get_notify_msg(client, chat_link, 10, cache.get(chat_link))
        if notify_msg:
            notify_msg_list.append(notify_msg)

    msg = "\n".join(notify_msg_list)
    # 推送TG
    send_message_to_notify_group(Settings.MY_NOTIFY_CHAT_ID, msg)
