from django.urls import path, include

from . import views
from home.api import views as api_view
# from rest_framework import routers
# from home.api import views as HomeApi
# route = routers.DefaultRouter()
# route.register('v1/api', HomeApi.HomeAPIVew, basename="Api")
# from home.api import viewsets as homeviewsets
# route = routers.DefaultRouter()
# route.register('v1/api', homeviewsets.HomeViewSet, basename="Api")

urlpatterns = [
    path("", views.index, name="index"),
    path("code/", views.code, name="code"),
    path('v1/api/', api_view.HomeAPIVew.as_view(), name="api"),

    # path('', include(route.urls))
]