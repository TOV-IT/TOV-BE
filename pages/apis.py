from rest_framework import generics, views
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
)

from pages.models import *
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response

from .serializers import (
    ComponentCreateSerializer,
)


class ComponentCreateAPIView(generics.CreateAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentCreateSerializer
    permission_classes = [AllowAny]
    # throttle_scope = 'create_post'

