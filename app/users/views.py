from rest_framework import viewsets
from .serializers import PaymentPlanSerializer, UserSerializer
from .models import PaymentPlan, User


class PaymentPlanViewSet(viewsets.ModelViewSet):
    queryset = PaymentPlan.objects.all()
    serializer_class = PaymentPlanSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
