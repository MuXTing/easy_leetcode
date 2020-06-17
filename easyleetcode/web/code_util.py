#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : xinfa.jiang
# @File    : code_all_in_map.py
import os




def get_file_read(path: str):
    pycode = open(path, encoding='utf-8').read()
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


