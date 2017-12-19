# coding: utf-8

from datetime import datetime

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseServerError
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from leancloud import Object
from leancloud import Query
from leancloud.errors import LeanCloudError
import json


class Customer(Object):
    def set_name(self, name):
        self.set("name", name)

    def set_phone(self, phone):
        self.set("phone", phone);

    def set_type(self, type):
        self.set("type", type);

    def get_name(self):
        return self.get("name")

    def get_phone(self):
        return self.get("phone")

    def get_type(self):
        return self.get("type")


class Content(Object):
    def set_text(self, text):
        set("text", text)

    def get_text(self):
        self.get("text")


class Record(Object):
    def set_customer(self, customer):
        set("customer", customer)

    def set_content(self, content):
        set("content", content)

    def get_customer(self):
        return self.get("customer")

    def get_content(self):
        return self.get("content")


def index(request):
    return render(request, 'index.html', {})


def current_time(request):
    return HttpResponse(datetime.now())


def customer_list(request):
    page = 0
    page_size = 0
    query = Query(Customer)
    try:
        page = int(request.GET.get("page"))
        page_size = int(request.GET.get("size"))
        if (page_size > 0):
            query.limit(page_size)
    except Exception as e:
        print(e)
    skip = page * page_size
    query.skip(skip)
    results = query.find()
    objs = []
    for result in results:
        objs.append(result.dump())
    return HttpResponse(json.dumps(objs))


class CustomerView(View):
    def get(self, request):
        return render(request, "customer.html")

    def post(self, request):
        content = request.POST.get('content')

        # todo = Todo(content=content)
        # try:
        #     todo.save()
        # except LeanCloudError as e:
        #     return HttpResponseServerError(e.error)
        # return HttpResponseRedirect(reverse('todo_list'))
        # try:
        #            todos = Query(Todo).descending('createdAt').find()
        #        except LeanCloudError as e:
        #            if e.code == 101:  # 服务端对应的 Class 还没创建
        #                todos = []
        #            else:
        #                raise e
        #        return render(request, 'todos.html', {
        #            'todos': [x.get('content') for x in todos],
        #        })
