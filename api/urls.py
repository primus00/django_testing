from django.urls import path
from rest_framework import routers

from .router import CustomReadOnlyRouter
from .views import UserViewSet, RandomViewSet

router = CustomReadOnlyRouter()
router.register('users', UserViewSet)
router.register('try', RandomViewSet, basename='try')
urlpatterns = router.urls