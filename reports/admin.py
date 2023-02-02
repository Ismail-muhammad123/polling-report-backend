from django.contrib import admin
from .models import Report, Ward, PollingUnit, AgentProfile


@admin.register(Ward)
class ReportAdmin(admin.ModelAdmin):
    list_display = [
        "local_government",
        "name",
        "added_at",
    ]



@admin.register(PollingUnit)
class PollingUnitAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "ward",
        "added_at",
    ]

@admin.register(AgentProfile)
class AgentProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    pass