import django.urls
from django.urls import path,include
from . import views
urlpatterns=[
    path ('', views.apiOverview, name='apiOverview'),
    path('student-list/',views.ShowAll,name='student-list'),
    path('student-detail/<int:pk>/',views.ShowStudent,name='student-detail'),
    path('student-create/', views.CreateStudent,name='student-create'),
    path('student-update/<int:pk>',views.UpdateStudent,name='student-update'),
    path('student-delete/<int:pk>',views.DeleteStudent,name='student-delete'),
    
]