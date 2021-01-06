from django.db import models

# Create your models here.
class LogItem(models.Model):
    ST_OPTIONS = [
        (0,'待處理'),
        (1,'處理中'),
        (2,'已結束'),
    ]
    subject = models.CharField('報修項目', max_length=255)
    description = models.TextField('報修內容')
    reporter = models.CharField('報修人', max_length=30)
    phone = models.CharField('連絡電話', max_length=30)
    ctime = models.DateTimeField('報修時間', auto_now_add=True)
    handler = models.CharField('處理人員', max_length=30)
    status = models.IntergerField(
                '處理進度',
                default=0,
                choices=ST_OPTIONS
            )
    comment = models.TextField('處理說明')
    utime = models.DateTimeField('更新時間', auto_now=True)

    def __str__(self):
        return self.reporter + ':' + self.subject