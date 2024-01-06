from django.contrib import admin

from track.models import Goal


class GoalAdmin(admin.ModelAdmin):

    def short_description(self, obj):
        return obj.description[:10]
    
    model = Goal
    list_display = ("short_description", "status", "target_date", "owner")

admin.site.register(Goal, GoalAdmin)
