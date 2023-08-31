from django.urls import path
from ProjectFinal import views

urlpatterns =[
    path('index', views.func_Index, name = 'index'),
    path('about', views.func_About, name = 'about'),
    path('blog', views.func_Blog, name = 'blog'),
    path('contact', views.func_Contact, name = 'contact'),
    path('services', views.func_Services, name = 'services'),

    path('make', views.func_Make, name ='make'),
    path('fairytale', views.func_Fairytale, name ='fairytale'),
]