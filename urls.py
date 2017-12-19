# coding: utf-8

from django.conf.urls import url
from django.views import static

import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^time/?$', views.current_time),
    url(r'^api/customer/list?$', views.customer_list),
    url(r'^customer/?$', views.CustomerView.as_view()),
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': 'static'}),
]
