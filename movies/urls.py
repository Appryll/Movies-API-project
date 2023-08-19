from rest_framework import routers
from .views import MoviesViewSet, MovieListTitleDescriptionFilter

router = routers.DefaultRouter()

router.register('', MoviesViewSet, basename='movies')
router.register('search', MovieListTitleDescriptionFilter, basename='search')

urlpatterns = router.urls