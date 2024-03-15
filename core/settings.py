# -*- coding: utf-8 -*-
# @Time    : 2024/3/14 1:46 下午
# @Author  : Hoey

class Settings():
    #### 推送机器人：掉用TG-BOT机器人，给群组发送消息，需要提前将机器人添加到群组 ####
    # 机器人的token
    MY_NOTIFY_BOT_TOKEN = "7118307959:AAE5hADqqaJ58Fw2lk_EciWVo4crBCLlO8I1"
    # 推送到哪个群组
    MY_NOTIFY_CHAT_ID = "-41335139841"

    #### 贴吧监控：爬取贴吧内容到文本并推送到TG ####
    # 贴吧监控：PT贴吧后缀
    PT_TIEBA_SUFFIX = 'pt&ie=utf-8&tab=main'
    # 贴吧监控：PT贴吧内容暂存文件
    TEMP_TIEBA_MSG_FILE = './baidu_temp_file.txt'
    # 贴吧监控：PT贴吧全链接
    TIEBA_URL = f'https://tieba.baidu.com/f?kw={PT_TIEBA_SUFFIX}'
    # 贴吧监控：过滤规则
    TIEBA_FILTER_KEY = '发'

    #### TG监控： 用于爬取TG群组消息 ####
    # TG监控： 需要申请API_ID
    API_ID = 148026821
    # TG监控： 需要申请API_HASH
    API_HASH = '54a599d3f86b00ab3eefe718ce56f4e01'
    # TG监控： 需要登陆TG手机号
    PHONE_NUM = '+158666642921'
    # TG监控： 需要爬取的群组
    CHAT_GROUPS = ['https://t.me/+KCkEpVCikBZjZjQ1']
    # TG监控： 缓存文件，用于存储消息最新偏移量
    TEMP_TG_MSG_FILE = './simple_cache.txt'
    # TG监控： 过滤规则
    TG_MSG_FILTER_LIST = ['发']
    # TG监控： 监控的链接
    CHAT_LINKS = ["https://t.me/M_Team_Chat", "https://t.me/+pjkIHKL3FYw4OWI1"]
