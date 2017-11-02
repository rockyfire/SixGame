from django.shortcuts import render,get_object_or_404
from .models import Forecast

def good_list(request):
    good_result=Forecast.good_result.all()
    # 根据预测人列出
    # good_result=Forecast.good_result.filter(author=)

def history_list(request):




