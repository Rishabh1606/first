from django.db import models

class user_profile(models.Model):
    Real_Name = models.CharField(max_length=100)
    Tz = models.CharField(max_length=100)

class user_activity(models.Model):
    user_profile_id = models.ForeignKey(user_profile, on_delete=models.CASCADE)
    Action_startTime = models.DateTimeField()
    Action_endTime = models.DateTimeField()

