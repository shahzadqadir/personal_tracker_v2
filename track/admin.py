from django.contrib import admin

from track.models import Goal, Objective


class GoalAdmin(admin.ModelAdmin):

    def short_description(self, obj):
        return obj.description[:10]
    
    model = Goal
    list_display = ("short_description", "status", "target_date", "owner")


class ObjectiveAdmin(admin.ModelAdmin):
    model = Objective
    list_display = ("short_description", "due_date", "effort_hours", "goal")


admin.site.register(Goal, GoalAdmin)
admin.site.register(Objective, ObjectiveAdmin)