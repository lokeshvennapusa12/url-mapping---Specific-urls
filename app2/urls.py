from django.urls import path
from app2.views import *
app_name='pra1'
urlpatterns=[
    path('prabhas/',prabhas,name='prabhas')
]