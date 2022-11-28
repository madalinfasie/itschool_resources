from django.contrib import admin

from mainapp import models


class MovieAdmin(admin.ModelAdmin):
    list_filter = ('release_date',)
    fieldsets = (
        (None, {
            'fields': ('title', 'release_date')
        }),
        ('Details', {
            'classes': ('collapse',),
            'fields': ('description',),
        }),
    )

admin.site.register(models.Movie, MovieAdmin)
