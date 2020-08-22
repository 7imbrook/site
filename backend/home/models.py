from django.db.models import Model, CharField, IntegerField, ForeignKey, CASCADE, BooleanField
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from enum import IntEnum

class SlugLocations(IntEnum):
  HOME = 1
  
  @classmethod
  def choices(cls):
    return [(key.value, key.name) for key in cls]

class Page(Model):
    type = IntegerField(choices=SlugLocations.choices())

class SlugMessage(Model):
    slug = CharField(max_length=140)
    page = ForeignKey(Page, on_delete=CASCADE)
    active = BooleanField()


def make_published(modeladmin, request, queryset):
    queryset.update(active=True)

def make_unpublished(modeladmin, request, queryset):
    queryset.update(active=False)

# Why not a decorator?
make_published.short_description = "Make Active"
make_unpublished.short_description = "Deactive"


class SlugMessageAdmin(ModelAdmin):
    list_display = ('slug', 'active')
    actions = [make_unpublished, make_published]


admin.site.register(Page)
admin.site.register(SlugMessage, SlugMessageAdmin)