# coding: utf-8

from gevent import monkey

monkey.patch_all()

import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# 设置 Django 项目配置文件
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
os.environ.setdefault("LC_APP_ID", "vLVbJinPOjCftQwyMRYj2l8P-gzGzoHsz")
os.environ.setdefault("LC_APP_MASTER_KEY", "d5sLfUj39WA3QGp9KLKCskWm")

import leancloud
from gevent.pywsgi import WSGIServer

from cloud import engine

APP_ID = "vLVbJinPOjCftQwyMRYj2l8P-gzGzoHsz";
MASTER_KEY = "d5sLfUj39WA3QGp9KLKCskWm";
PORT = int(os.environ['LC_APP_PORT'])

leancloud.init(APP_ID, master_key=MASTER_KEY)

application = engine

if __name__ == '__main__':
    # 只在本地开发环境执行的代码
    server = WSGIServer(('localhost', PORT), application)
    server.serve_forever()
