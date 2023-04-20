from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=False, blank=False)
    leetcode_id = models.CharField(max_length=150)
    hackerrank_id = models.CharField(max_length=150)
    codechef_id = models.CharField(max_length=150)
