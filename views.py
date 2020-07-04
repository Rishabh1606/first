from django.shortcuts import render
from rest_framework import viewsets

from .serializers import UserSerializer, ActivitySerializer, MapSerializer
from .models import User, Activity, MappTable
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def user_information(request):
    mainDic = {"ok":True}
    all_data = user_profile.objects.all()
    for i in all_data:
        dic_Data = {"id":i.id, "real_name":i.Real_Name, "tz":i.Tz }
        activity_data = user_activity.objects.filter(user_profile_id=i.id)
        listData = []
        for j in activity_data:
            listData.append({"start_time":j.Action_startTime, "end_time":j.Action_endTime})
    mainDic["member"] = mainDic
    return Response(PostSerializer, status=200)
            
        
        
