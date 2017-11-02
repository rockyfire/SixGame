from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.good_list,name='post_list'),
    url(r'^histroy$',views.history_list,name='history_list')
]
