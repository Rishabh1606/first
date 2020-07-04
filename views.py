from django.shortcuts import render
from rest_framework import viewsets

from .serializers import UserSerializer, ActivitySerializer, MapSerializer
from .models import User, Activity, MappTable


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
        # .values_list(action_id__Action_startTime, action_id__Action_endTime,user_id__id)
    # member = queryset
    serializer_class = UserSerializer
