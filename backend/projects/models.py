from django.db import models
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from rest_framework import serializers


class Project(models.Model):
    name = models.CharField(max_length=80)


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name']


class ProjectAdmin(ModelAdmin):
    list_display = ("name",)


admin.site.register(Project, ProjectAdmin)
