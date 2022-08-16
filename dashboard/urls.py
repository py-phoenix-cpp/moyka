from django.urls import path
from dashboard.views import *

urlpatterns = [
    path('', Index, name='index'),
    path('account/', Account_setting, name='account_setting'),
]