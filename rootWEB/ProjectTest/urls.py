from django.urls import path
from ProjectTest import views

urlpatterns =[
    path('', views.funcTest ),
    path('home_url', views.funcTestHome, name='test_home_url'),
    path('result_url', views.funcTestResult, name ='test_result_url'),
    path('final', views.funcTestFinal, name ='final'),
]