from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse
from .models import LogItem

# Create your views here.
# 報修項目列表
class LogList(ListView):
  model = LogItem
  ordering = ['-id']

# 檢視報修項目
class LogView(DetailView):
  model = LogItem

# 新增報修項目
class LogCreate(CreateView):
  model = LogItem
  # 新增時只顯示需填寫的部份欄位
  fields = ['subject', 'description', 'reporter', 'phone']

  def get_success_url(self):
    return reverse('log_list')

# 回覆維修進度
class LogReply(UpdateView):
  model = LogItem
  # 回覆時僅顯示相關欄位
  fields = ['handler', 'status', 'comment']

  def get_success_url(self):
    return reverse('log_view', kwargs={'pk': self.object.id})