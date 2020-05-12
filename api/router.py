from rest_framework.routers import Route, DynamicRoute, SimpleRouter

"""
    @todo Add new ApiConfig
    @body There is a requirement of destroy action <br> ![img](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.M9AsZ7Sm6Qq-LXpY92Tt2AHaEK%26pid%3DApi&f=1) 
"""

class CustomReadOnlyRouter(SimpleRouter):
    """
    A router for read-only APIs, which doesn't use trailing slashes.
    """
    routes = [
        Route(
            url=r'^{prefix}$',
            mapping={'get': 'list'},
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
        Route(
            url=r'^{prefix}/{lookup}$',
            mapping={'get': 'retrieve'},
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        ),
        Route(
            url=r'^{prefix}/{lookup}$',
            mapping={'get': 'update'},
            name='{basename}-update',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        ),
        Route(
            url=r'^{prefix}/{lookup}$',
            mapping={'get': 'destroy'},
            name='{basename}-destroy',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        ),
        Route(
            url=r'^{prefix}/{lookup}$',
            mapping={'get': 'create'},
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        ),
        DynamicRoute(
            url=r'^{prefix}/{lookup}/{url_path}$',
            name='{basename}-{url_name}',
            detail=True,
            initkwargs={}
        )
    ]