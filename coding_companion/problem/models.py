from django.db import models


class TopicTag(models.Model):
    tag = models.CharField(max_length=250)


class Problem(models.Model):
    title = models.CharField(max_length=250)
    likes = models.IntegerField()
    category = models.CharField(max_length=250)
    difficulty = models.CharField(max_length=250)
    has_solution = models.BooleanField()
    tag = models.ManyToManyField(TopicTag, related_name="problems")
