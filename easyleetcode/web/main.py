#!/usr/bin/env python
# -*- coding: utf-8 -*-


import uvicorn
from fastapi import FastAPI

import easyleetcode.config as config
import easyleetcode.web.server as a_server
import easyleetcode.web.utils as utils

app = FastAPI()
app.mount("/static", config.statics, name="static")

app.include_router(a_server.router)


def run(host="127.0.0.1", port=8080, py_cmd_path='python '):
    '''

    :param host: host
    :param port: port
    :param py_cmd_path:python exe path/cmd
    :return:
    '''
    print('your host is :', host)
    print('your port is :', port)
    print('your python execute path is :', py_cmd_path, '(use command:', py_cmd_path, ' xxx.py to run python)')
    print('If you run error in Windows platform,tell me .Because Windows platform I have\'t test')

    config.templates.env.variable_start_string = '{['
    config.templates.env.variable_end_string = ']}'
    a_server.python_path = py_cmd_path
    # every times running,path config.count_day 's count +=1 (running count log)
    utils.add_file_txt_count(config.count_day)
    print('_____running:____')
    print('please web browser', 'http://%s:%s' % (str(host), str(port)))
    # uvicorn.run(app=app, host=host, port=port, log_level="error")
    uvicorn.run(app=app, host=host, port=port)


if __name__ == '__main__':
    run()
