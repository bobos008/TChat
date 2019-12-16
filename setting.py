# coding=utf-8

import os


# mysql配置
mysql_options = {

}

# app配置
settings = {
    'template_path': os.path.join(os.path.dirname(__file__), "template"),
    'static_path': os.path.join(os.path.dirname(__file__), "static"),
    'xsrf_cookies': True,
    'cookie_secret': '8e1913e2-1fde-11ea-8edd-50e549bedfee',
    'login_url': '/login',
    'debug': True
}

# 日志
log_path = os.path.join(os.path.dirname(__file__), 'logs/log')
