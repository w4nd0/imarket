# apps/urls.py
from .views import CartModelViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(prefix=r'cart', viewset=CartModelViewSet)

urlpatterns = router.urls
