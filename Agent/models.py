from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  # Django Admin


# class TodayManager(models.Manager):
#     def get_queryset(self):
#         return super(TodayManager,self).get_queryset().filter()

# Create your models here.
# 历史结果
class History(models.Model):
    Six_number = models.CharField(max_length=100)  # 期数
    Six_date = models.DateTimeField()  # 日期
    Six_slave = models.CharField(max_length=30)  # 平码
    Six_master = models.CharField(max_length=10)  # 特码
    Six_oddSeve = models.CharField(max_length=10)  # 单双
    Six_bigSmall = models.CharField(max_length=10)  # 大小
    Six_He_oddSeve = models.CharField(max_length=10)  # 合数单双
    Six_He_bigSmall = models.CharField(max_length=10)  # 合数大小

    # today=TodayManager()

    class Meta:
        ordering = ('-Six_date',)

    def __str__(self):
        return self.Six_number

    def get_absolute_url(self):
        return reverse('agent:detail_day',
                       args=[
                           self.Six_date.year,
                           self.Six_date.strftime("%m"),
                           self.Six_date.strftime("%d"),
                       ])


class GoodManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(result='good')


# 个人预测
class Forecast(models.Model):
    # 状态选择 草稿和发布
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    # 预测结果 中与不中
    FORECAST_RESULT = (
        ('good', 'Good'),
        ('try', 'Try'),
    )
    number = models.CharField(max_length=100)

    title = models.CharField(max_length=250)
    # slug就是一个短标签，该标签只包含字母，数字，下划线或连接线。
    # 我们将通过使用slug字段给我们的blog帖子构建漂亮的，友好的URLs。
    # 我们给该字段添加了unique_for_date参数，
    # 这样我们就可以使用 日期 和 帖子 的slug来为所有帖子构建URLs
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name="blog_post")
    body = models.TextField()

    publish = models.DateTimeField(default=timezone.now)
    # auto_now_add，当一个对象被创建的时候这个字段会自动保存当前日期。
    created = models.DateTimeField(auto_now_add=True)
    # auto_now，当我们更新保存一个对象的时候这个字段将会自动更新到当前日期。
    updated = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    result = models.CharField(max_length=10,
                              choices=FORECAST_RESULT,
                              default='good')
    good_i = GoodManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
