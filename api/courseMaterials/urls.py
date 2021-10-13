from django.urls import path
from . import views

urlpatterns= [
    path('',views.SemesterView.as_view(), name='semester_view'),
    path('<str:semester>/create/', views.CourseView_create.as_view(), name='course_view_create'),    
    path('<slug:slug>/',views.CourseView.as_view(),name='course_view'),
    path('<str:semester>/<slug:slug>/', views.LectureView.as_view(), name='lecture_view'),
    path('<str:semester>/<str:slug>/create/', views.LectureView_create.as_view(), name='lecture_view_create'),    
    path('<str:semester>/<str:course>/<slug:slug>/', views.LectureView2.as_view(), name='lecture_view_lec'),
    path('<str:semester>/<str:course>/<slug:slug>/update/', views.LectureView_update.as_view(), name='lecture_view_update'),
    path('<str:semester>/<str:course>/<slug:slug>/delete/', views.LectureView_delete.as_view(), name='lecture_view_delete'),

]