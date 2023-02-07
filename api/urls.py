from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

urlpatterns = [

    path('', views.getRoutes),
    path('developers/', views.ProfileLC.as_view()),
    path('projects/', views.ProjectLC.as_view()),
    path('project/<str:pk>/', views.ProjectRUD.as_view()),
    path('developer/<str:pk>/', views.ProfileRUD.as_view()),
  
]


# router = DefaultRouter()
# router.register('profileLC', views.ProfileLC.as_view(),basename="profilelc")
# router.register('projectLC', views.ProjectLC.as_view(),basename="projectlc")
# router.register('profileRUD', views.ProfileRUD.as_view(),basename="profilerud")
# router.register('projectRUD', views.ProjectRUD.as_view(),basename="projectrud")



# urlpatterns = [
#   path('', include(router.urls)),
#   path('auth/',include('rest_framework.urls',namespace='rest_framework'))
# ]

# #AttributeError: 'function' object has no attribute 'get_extra_actions'

