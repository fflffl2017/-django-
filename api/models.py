from __future__ import unicode_literals
from django.db import models


class flag_table(models.Model):
#    flag = models.CharField(max_length=40)
#    osystem = models.CharField(max_length=10)
#    score = models.IntegerField()
#    title_name = models.CharField(max_length=20)
#    title_description = models.CharField(max_length=40)
#    degree_of_difficulty = models.CharField(max_length=2)
#    team_name = models.CharField(max_length=20)
#    ip_address = models.GenericIPAddressField()
#    submit_time = models.DateTimeField(auto_now=True)
#    submit_flag = models.CharField(max_length=40)
#   result = models.IntegerField()
#    times = models.IntegerField()

    time_num = models.IntegerField()
    timu_flag = models.CharField(max_length=40)



class yunwei_table(models.Model):
    timu_ID = models.IntegerField()
    timu_os = models.CharField(max_length=10)
    timu_name=models.CharField(max_length=20)
    timu_score = models.IntegerField()
    timu_result = models.IntegerField()
    timu_date = models.DateTimeField(auto_now=True)
    timu_defensive=models.IntegerField()
    timu_ip=models.CharField(max_length=20)