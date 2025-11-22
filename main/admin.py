from django.contrib import admin
from .models import Event, SocialAction, Photo

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location')
    inlines = [PhotoInline]

@admin.register(SocialAction)
class SocialActionAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    inlines = [PhotoInline]

admin.site.register(Photo)
