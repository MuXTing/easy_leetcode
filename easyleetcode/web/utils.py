#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : xinfa.jiang
# @File    : utils.py
import os
from easyleetcode.config import root_path


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


def del_file(path):
    os.remove(path)


def get_all_code_map(code_dir=os.path.join(root_path, 'leetcodes'),
                     code_md_dir=os.path.join(root_path, 'leetcodes_md')):
    code_map = {}
    code_map[-1] = ('root', code_dir, code_md_dir)
    for fname in os.listdir(code_dir):
        try:
            idx = int(fname.split('_')[1])
            name = fname[:-3]
        except:
            continue
        path = os.path.join(code_dir, fname)
        md_path = os.path.join(code_md_dir, name + '.md')
        code_map[idx] = (name, path, md_path)
    return code_map


def load_data():
    # code map by id as key
    code_map = get_all_code_map()
    # code map by name as key
    code_name_map = {}
    for kid in sorted(code_map):
        name, code_path, md_path = code_map[kid]
        code_name_map[name] = (kid, code_path, md_path)

    code_name_list = []
    for kid in sorted(code_map):
        name, _, _ = code_map[kid]
        if name == 'root':
            continue
        title = name[2:].replace('_', ' ')
        code_name_list.append([kid, name, title])
    code_name_list = sorted(code_name_list)
    return code_map, code_name_map, code_name_list
