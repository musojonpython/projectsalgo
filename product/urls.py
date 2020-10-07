from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ProductModelViewSet

router = SimpleRouter()
router.register('', ProductModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]