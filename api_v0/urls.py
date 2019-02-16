from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'users', UserViewSet)


urlpatterns = router.urls
