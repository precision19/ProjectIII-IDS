from django.db import models

# Create your models here.
class Data(models.Model):
    duration = models.IntegerField()
    protocol = models.CharField(max_length=5)
    service = models.CharField(max_length=30)
    flag = models.CharField(max_length=5)
    src_bytes = models.IntegerField()
    dst_bytes = models.IntegerField()
    land = models.IntegerField()
    wrong_fragments = models.IntegerField()
    urgent = models.IntegerField()
    hot = models.IntegerField()
    num_failed_logins = models.IntegerField()
    logged_in = models.IntegerField()
    num_compromise = models.IntegerField()
    root_shell = models.BooleanField()
    su_attempted = models.BooleanField()
    num_root = models.IntegerField()
    num_file_creations = models.IntegerField()
    num_shell = models.IntegerField()
    num_access_file = models.IntegerField()
    num_outbound_cmd = models.IntegerField()
    is_hot_login = models.BooleanField()
    is_guest_login = models.BooleanField()
    count = models.IntegerField()
    srv_count = models.IntegerField()
    serror_rate = models.FloatField()
    srv_serror_rate = models.FloatField()
    rerror_rate = models.FloatField()
    srv_rerror_rate = models.FloatField()
    same_srv_rate = models.FloatField()
    diff_srv_rate = models.FloatField()
    srv_diff_host_rate = models.FloatField()