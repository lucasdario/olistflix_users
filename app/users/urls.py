from django.urls import include, path
from rest_framework import routers
from .views import PaymentPlanViewSet, UserViewSet

router = routers.DefaultRouter()

router.register(r'payments', PaymentPlanViewSet, basename='payments')
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
