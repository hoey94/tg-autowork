# -*- coding: utf-8 -*-
# @Time    : 2024/3/14 4:25 下午
# @Author  : Hoey


def not_in_list2(fayao_list, temp_file_list):
    l_list = []
    for x in fayao_list:
        if x not in temp_file_list:
            l_list.append(x)

    return l_list
