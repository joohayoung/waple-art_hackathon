from django.contrib import admin
from .models import ArtInfoDB, PerformanceDB, FestivalDB, ArtWorkDB
# Register your models here.

class ArtInfoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'category',)

class PerformanceAdmin(admin.ModelAdmin):
    list_display = ('pk', 'artinfo','cl',)

class FestivalAdmin(admin.ModelAdmin):
    list_display = ('pk', 'artinfo',)

admin.site.register(ArtInfoDB, ArtInfoAdmin)
admin.site.register(PerformanceDB, PerformanceAdmin)
admin.site.register(FestivalDB, FestivalAdmin)
admin.site.register(ArtWorkDB)