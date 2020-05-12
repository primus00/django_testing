from .router import CustomReadOnlyRouter
from .views import UserViewSet, RandomViewSet

"""
    @todo Add route for login api.urls
    @body There is a requirement of destroy action <br> ![img](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.M9AsZ7Sm6Qq-LXpY92Tt2AHaEK%26pid%3DApi&f=1) 
"""

router = CustomReadOnlyRouter()
router.register('users', UserViewSet)
router.register('try', RandomViewSet, basename='try')
urlpatterns = router.urls