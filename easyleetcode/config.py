#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : xinfa.jiang
# @File    : config.py
import os
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

root_path = os.path.dirname(__file__)

statics = StaticFiles(directory=os.path.join(root_path, 'web/static'))
templates = Jinja2Templates(directory=os.path.join(root_path, 'web/templates'))
python_path = 'python3 '
count_day = os.path.join(root_path, 'logs/count_day.txt')
count_view_code = os.path.join(root_path, 'logs/count_view_code.txt')

