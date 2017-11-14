from django.shortcuts import render, get_object_or_404
from .models import Forecast, History

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
import csv
import datetime

# class GoodListView(ListView):
#     queryset = Forecast.good_result.all()
#     context_object_name = 'posts'
#     paginate_by = 3
#     template_name = ''


# def good_list(request):
#     good_result = Forecast.good_result.all()
# 根据预测人列出
# good_result=Forecast.good_result.filter(author=)
"""分页"""

"""
paginator = Paginator(good_result, 3)
page = request.GET.get('page')
try:
    posts = paginator.page(page)
except PageNotAnInteger:
    posts = paginator.page(1)
except EmptyPage:
    posts = paginator.page(paginator.num_pages)
return render(request,
              'blog/post/list.html',
              {'posts': posts})
"""


def import_data(request):
    with open('/home/candy/Desktop/git/SixGame/data_sixhistory.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = History.objects.get_or_create(
                Six_number=row[0],
                Six_date=datetime.strptime(row[1], "%Y/%m/%d"),
                Six_slave=row[2],
                Six_master=row[3],
                Six_oddSeve=row[4],
                Six_bigSmall=row[5],
                Six_He_oddSeve=row[6],
                Six_He_bigSmall=row[7],
            )
    return render(request, 'agent/success.html')


def history_list(request, year='2017'):
    historys_list = History.objects.filter(Six_date__year=year)
    return render(request, 'agent/history/history.html', {'historys_list': historys_list})


def history_detail(request, year, num=None, month='01', day='01'):
    # historys_list = get_object_or_404(History,
    historys_list = History.objects.filter(
        Six_date=datetime.date(int(year), int(month), int(day))
        # Six_date__year=year,
        # Six_date__month=month,
        # Six_date__day=day,
    )
    historys_list = History.objects.filter(
        Six_date__year=year,
        Six_number=num,
    )
    return render(request, 'agent/history/history.html', {'historys_list': historys_list})

# def realtime_list(request):
