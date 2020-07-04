from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    Real_Name = models.CharField(max_length=100)
    Tz = models.CharField(max_length=100)

class Activity(models.Model):
    action_id =models.AutoField(primary_key=True)
    Name_of_action = models.CharField(max_length=50)
    Action_startTime = models.DateTimeField()
    Action_endTime = models.DateTimeField()

class MappTable(models.Model):
    activity_mapping_id = models.AutoField(primary_key=True)
    action_id = models.ForeignKey(Activity, to_field="action_id", on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, to_field="id", on_delete=models.CASCADE)
