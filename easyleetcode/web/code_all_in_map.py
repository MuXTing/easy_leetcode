#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : xinfa.jiang
# @File    : code_all_in_map.py
from easyleetcode.config import root_path
import os


def get_all_code_map(code_dir=os.path.join(root_path, 'leetcodes'),
                     code_md_dir=os.path.join(root_path, 'leetcodes_md')):
    code_map = {}
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


def get_file_read(path: str):
    pycode = open(path,encoding='utf-8').read()
    return pycode


def call_py_file(path, python_path='python3 '):
    try:
        s = os.popen(python_path + path, 'r', 1)
        res = s.read()
        out = []
        for line in res.splitlines():
            out.append(line)
        return out
    except:
        return ['null']


if __name__ == '__main__':
    code_map = get_all_code_map()
