from rest_framework import generics
from apps.core.models import Mag, User, Prod
from apps.core.serializers import MagSerializer, UserSerializer, ProdSerializer

class UserViewSet(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MagViewSet(generics.ListCreateAPIView):
    queryset = Mag.objects.all()
    serializer_class = MagSerializer

class ProdViewSet(generics.ListCreateAPIView):
    queryset = Prod.objects.all()
    serializer_class = ProdSerializer