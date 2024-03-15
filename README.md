
# 背景

主运行程序：
```
tieba.py： 贴吧监控并推送TG
tg_scrapper.py: TG群组监控并推送TG
```

傻瓜式运行，其他的都不用动，按照下面操作可以保证运行起来。第一次运行可以先按照下面的配置先运行起来。

# settings.py介绍

只需要对settings.py进行设置，就可以运行上面两个主程序。如果你需要定制化，就需要看懂代码，进行调整。

settings.py中有几个要改的参数，标记一下:
```
MY_NOTIFY_BOT_TOKEN = "7118307959:AAE5hADqqaJ58Fw2lk_EciWVo4crBCLlO8I1"
MY_NOTIFY_CHAT_ID = "-41335139841"
API_ID = 148026821
API_HASH = '54a599d3f86b00ab3eefe718ce56f4e01'
PHONE_NUM = '+158666642921'
CHAT_LINKS = ["https://t.me/M_Team_Chat", "https://t.me/+pjkIHKL3FYw4OWI1"]
```

下面简单描述以下如何获得上面的参数，如果你知道如何做，请忽略下面内容。

# 配置
创建机器人，获取下面参数

BOT_TOKEN, 将BOT_TOKEN 填写到settings.py MY_NOTIFY_BOT_TOKEN

到TG创建群组，将机器人拉到群组，获取下面群组参数

CHAT_ID , 将BOT_TOKEN 填写到settings.py MY_NOTIFY_CHAT_ID

通过https://my.telegram.org/apps 这个网站，创建application应用，获得API_ID和API_HASH 填写到settings.py

PHONE_NUM 记得改成自己的

CHAT_LINKS 是要监控的群组信息，比如我要监控MT群组，找到群组的分享链接"https://t.me/M_Team_Chat

其他群组以此类推