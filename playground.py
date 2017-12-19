# coding: utf-8
from views import Customer
from leancloud import Query
import json
import os

# 设置 Django 项目配置文件
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

import leancloud

APP_ID = os.environ['LC_APP_ID']
MASTER_KEY = os.environ['LC_APP_MASTER_KEY']
PORT = int(os.environ['LC_APP_PORT'])

leancloud.init("vLVbJinPOjCftQwyMRYj2l8P-gzGzoHsz", master_key="d5sLfUj39WA3QGp9KLKCskWm")

# query = Query("Customer")
#
# results = query.find()
# objs=[]
# for result in results:
#      objs.append(result.dump())
# print json.dumps(objs)
# customer=Customer()
# customer.set_name("江磊")
# customer.set_phone("18408249115")
# customer.set_type("西充农商行员工")
# customer.save()
import xlrd
import sys

book = xlrd.open_workbook("contact.xlsx")
sh = book.sheet_by_index(0)
customers=[]
for rx in range(1, sh.nrows):
    phone=str(int(sh.cell_value(rx, 1)))
    name=sh.cell_value(rx, 0)
    type=sh.cell_value(rx, 9)
    customer=Customer()
    customer.set_name(name)
    customer.set_phone(phone)
    customer.set_type(type)
    customers.append(customer)
Customer.save_all(customers)


