from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('new/', views.new_friend, name='new_friend'),
    path('person/<slug:friend_name>/', views.chosed_friend, name='chosed')
]
