<p align="center"><a href="https://dataease.io"><img src="https://dataease.oss-cn-hangzhou.aliyuncs.com/img/dataease-logo.png" alt="DataEase" width="300" /></a></p>
<h3 align="center">MoviePilot</h3>
<p align="center">
  <a href="https://www.gnu.org/licenses/gpl-3.0.html"><img src="https://img.shields.io/github/license/dataease/dataease?color=%231890FF" alt="License: GPL v3"></a>
  <a href="https://app.codacy.com/gh/dataease/dataease?utm_source=github.com&utm_medium=referral&utm_content=dataease/dataease&utm_campaign=Badge_Grade_Dashboard"><img src="https://app.codacy.com/project/badge/Grade/da67574fd82b473992781d1386b937ef" alt="Codacy"></a>
  <a href="https://github.com/dataease/dataease"><img src="https://img.shields.io/github/stars/dataease/dataease?color=%231890FF&style=flat-square" alt="Stars"></a>
</p>





<p align="center'>
<a href="./README.md">English</a>|<a href="readme/README.zh_CN.md">简体中文</a>
</p>


# Background

Main running programs:
```
tieba.py: Monitors Tieba and pushes to Telegram (TG)
tg_scrapper.py: Monitors TG groups and pushes to TG
```

Easy to run, no need to do anything else. Follow the operations below to ensure it runs. For the first run, you can start it by following the configuration below.

# Introduction to settings.py

You only need to set settings.py to run the two main programs above. If you need customization, you will need to understand the code and make adjustments.

There are several parameters in settings.py that need to be modified, marked as follows:
```
MY_NOTIFY_BOT_TOKEN = "7118307959:AAE5hADqqaJ58Fw2lk_EciWVo4crBCLlO8I1"
MY_NOTIFY_CHAT_ID = "-41335139841"
API_ID = 148026821
API_HASH = '54a599d3f86b00ab3eefe718ce56f4e01'
PHONE_NUM = '+158666642921'
CHAT_LINKS = ["https://t.me/M_Team_Chat", "https://t.me/+pjkIHKL3FYw4OWI1"]
```

Below is a brief description of how to obtain the parameters above. If you know how to do it, please ignore the following content.

# Configuration
1. Create a bot to obtain the BOT_TOKEN.
2. Fill in BOT_TOKEN into MY_NOTIFY_BOT_TOKEN in settings.py.
3. Create a group on TG, add the bot to the group, and obtain the group parameter CHAT_ID.
4. Fill in CHAT_ID into MY_NOTIFY_CHAT_ID in settings.py.
5. Visit https://my.telegram.org/apps, create an application, and get API_ID and API_HASH. Fill them in settings.py.
6. Remember to change PHONE_NUM to your own number.
7. CHAT_LINKS are the group information to monitor. For instance, if you want to monitor the MT group, find the group's share link like https://t.me/M_Team_Chat. Add other group links accordingly.

# Debug
After configuration, run the two main programs above separately. Test to see if it can push to the TG group. Pay attention to the logs for error records.
