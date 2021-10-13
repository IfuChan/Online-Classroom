from django.urls import include, path
from rest_framework import routers
from api import views
from . import views


from django.urls import path

router = routers.DefaultRouter()
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    #path('', include(router.urls)),
    path('', views.apiOverview, name='apiOverview'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('user-list/',views.showAllUser,name='user list'),
    path('user-detail/<int:pk>',views.showUser,name='user detail'),
    path('user-create/',views.createUser,name='user create'),
    path('user-update/<int:pk>',views.updateUser,name='user update'),
    path('user-delete/<int:pk>',views.deleteUser,name='user delete'),
    #path('login/',views.LoginView.as_view(),name='user login'),
    path('login/',views.loginUser,name='user login'),
    path('course-create/',views.createCourse,name='course create'),
    path('course-list/',views.showAllCourse,name='course list'),
    path('lecture-create/',views.createLecture,name='lecture create'),
    path('lecture-list/',views.showAllLecture,name='lecture list'),

    
    
]