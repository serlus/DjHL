from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from .user import views

# Obs.: All endpoints need to be registered into this router

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
]
