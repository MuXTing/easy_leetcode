#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : xinfa.jiang
# @File    : server.py
import os
from fastapi import APIRouter

from fastapi import Request
from easyleetcode.config import templates
from easyleetcode.web.code_all_in_map import get_all_code_map, get_file_read, call_py_file
from easyleetcode.web.Items import Item
import easyleetcode.web.utils as utils
import easyleetcode.config as config

router = APIRouter()

python_path = 'python3 '


@router.get('/')
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": 'Easy Leetcode'})


@router.get('/help')
async def help(request: Request):
    return templates.TemplateResponse("help.html", {"request": request, "message": 'Easy Leetcode'})


@router.get('/about')
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request, "message": 'Easy Leetcode'})


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
    title = name[2:].replace('_', ' ')
    code_name_list.append([kid, name, title])


@router.get('/view')
async def view(request: Request):
    count_day = utils.get_file_txt_count(config.count_day)
    count_view_code = utils.get_file_txt_count(config.count_view_code)
    data = {
        'all_num': len(code_name_list),
        'count_day': count_day,
        'count_view_code': count_view_code,
        'code_name_list': code_name_list
    }
    return templates.TemplateResponse("code_list.html", {"request": request, "data": data, "message": "Leetcode List"})


@router.get('/code/{name}')
async def view_code(request: Request, name: str = '001_Two_Sum'):
    # 代码路径
    code_path = code_name_map[name][1]
    # 代码markdwon路径
    code_md_path = code_name_map[name][2]
    code_str = get_file_read(code_path)
    code_md_str = get_file_read(code_md_path)
    code_res = '\n'.join(call_py_file(code_path, python_path))
    data = {
        'code_str': code_str,
        'code_md_str': code_md_str,
        'name': name,
        'code_res': code_res
    }
    # every times view code,path config.count_view_code 's count +=1 (view code count log)
    utils.add_file_txt_count(config.count_view_code)
    return templates.TemplateResponse("code_view.html", {"request": request, "data": data, "message": name})


@router.put('/save')
async def save(item: Item):
    name = item.name
    # python code
    code_str = item.code_str
    # python code's Markdown note
    code_md_str = item.code_md_str
    # python code's path
    code_path = code_name_map[name][1]
    # python code's Markdown note 's path
    code_md_path = code_name_map[name][2]
    if code_str is not None:
        with open(code_path, 'w', encoding='utf-8') as of:
            of.write(code_str)
    if code_md_str is not None:
        with open(code_md_path, 'w', encoding='utf-8') as of:
            of.write(code_md_str)
    return {
        'status': 'success',
        'name': name
    }


@router.put('/run')
async def router_run(item: Item):
    name = item.name
    code_str = item.code_str
    # code's python path, to temp path
    code_path = code_name_map[name][1].replace('.py', '_temp.py')
    with open(code_path, 'w', encoding='utf-8') as of:
        of.write(code_str)
    code_res = '\n'.join(call_py_file(code_path, python_path))
    # rm temp path
    os.remove(code_path)

    return {
        'status': 'success',
        'code_res': code_res,
        'name': name
    }


@router.get('/md/{name}')
async def view_md(request: Request, name: str = '001_Two_Sum'):
    # 代码markdwon路径
    code_md_path = code_name_map[name][2]
    code_md_str = get_file_read(code_md_path)
    data = {
        'code_md_str': code_md_str,
        'name': name,
    }
    return templates.TemplateResponse("md.html", {"request": request, "data": data, "message": name})
