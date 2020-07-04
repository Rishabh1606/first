from rest_framework import serializers
from .models import User, Activity, MappTable

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'Real_Name', 'Tz')

class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        fields = ('action_id', 'Name_of_action', 'Action_startTime', 'Action_endTime')

class MapSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MappTable
        fields = ('activity_mapping_id', 'action_id', 'user_id')