from django.urls import path
from . import views


app_name = 'loginRegApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('createuser/', views.createuser, name='createuser'),
    path('success/', views.success, name='success'),
]
