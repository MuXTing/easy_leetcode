#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : xinfa.jiang
# @File    : utils.py

def add_file_txt_count(file_path):
    count = 0
    try:
        with open(file_path, encoding='utf-8', mode='r') as f:
            txt = f.read()
            txt = txt.replace('\n', '').strip()
            count = int(txt)
    except:
        count = 0
    count += 1
    with open(file_path, encoding='utf-8', mode='w') as f:
        f.write(str(count))


def get_file_txt_count(file_path):
    count = 0
    try:
        with open(file_path, encoding='utf-8', mode='r') as f:
            txt = f.read()
            txt = txt.replace('\n', '').strip()
            count = int(txt)
    except:
        count = 0
    return count
