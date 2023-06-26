from django.db import models
from django.contrib import admin
from .models import Problem, TopicTag


class TopicTagInline(admin.TabularInline):
    model = Problem.tag.through


class ProblemAdmin(admin.ModelAdmin):
    inlines = [TopicTagInline]


admin.site.register(TopicTag)
admin.site.register(Problem, ProblemAdmin)
