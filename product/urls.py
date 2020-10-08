from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ProductModelViewSet, EnterProductModelViewSet, ExpenseProductModelViewSet

router = SimpleRouter()
router.register('', ProductModelViewSet)
router.register('add', EnterProductModelViewSet)
router.register('take', ExpenseProductModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]