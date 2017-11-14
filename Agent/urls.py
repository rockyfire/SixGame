from django.conf.urls import url
from . import views
from .models import History, Forecast

urlpatterns = [
    # url(r'^good/', views.good_list, name='good_list'),
    # url(r'^add_data',views.import_data,name="add_data"),
    url(r'^history/$', views.history_list, name='history_list'),
    url(r'^history/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', views.history_detail, name='detail_day'),
    url(r'^history/(?P<num>\d{0,3})/(?P<year>\d{4})/$', views.history_detail, name='detail_num'),
    # url(r'^realtime/', views.realtime_list, name='realtime_list'),
]
