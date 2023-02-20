from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('new/', views.new_friend, name='new_friend')
]
