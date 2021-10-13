from django.urls import path
from . import views

urlpatterns= [
    path('', views.index, name='index'),
    path('register/', views.register, name='user_register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('record/', views.user_rec, name='user_rec'),
    path('notes/', views.notes, name='notes'),
    path('note', views.note, name='note'),
    path('notes/note', views.note, name='note'),

]