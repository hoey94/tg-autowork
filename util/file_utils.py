# -*- coding: utf-8 -*-
# @Time    : 2024/3/14 1:58 下午
# @Author  : Hoey
import os


def read_temp_file(temp_file):
    """
    1. encoding=不能省，因为使用的是位置传递参数
    2. 使用with open，省掉 close的动作
    """
    if not os.path.exists(temp_file):
        with open(temp_file, 'w') as file:
            pass

    with open(temp_file, 'r', encoding='UTF-8') as f:
        l_list = []
        for line in f:
            l_list.append(line.replace('\n', ''))
        return l_list


def append2_temp_file(temp_file, my_list):
    with open(temp_file, "a") as file:
        for item in my_list:
            file.write("%s\n" % item)

