from django.shortcuts import render

from app1.models import Flats
from rest_framework import viewsets,permissions
from .serializers import FlatSerializer


class FlatView(viewsets.ModelViewSet):
    queryset=Flats.objects.all()
    serializer_class=FlatSerializer
    permission_classes=(permissions.IsAuthenticated,)