from .router import CustomReadOnlyRouter
from .views import UserViewSet, RandomViewSet


"""
    @todo Add models api.urls
    @body There is a requirement of destroy action \
    @body ### is a requirement of destroy action \ 
    @body There is a requirement of destroy action \
    @body * is a requirement of destroy action \
    @body * is a requirement of destroy action \ 
    @body - [ ] is a requirement of destroy action \
"""


router = CustomReadOnlyRouter()
router.register('users', UserViewSet)
router.register('try', RandomViewSet, basename='try')
urlpatterns = router.urls