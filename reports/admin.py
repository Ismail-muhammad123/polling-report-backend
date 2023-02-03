from django.contrib import admin
from .models import Report, Ward, PollingUnit, AgentProfile


@admin.register(Ward)
class WardAdmin(admin.ModelAdmin):
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
    def full_name(self, obj):
        return obj.user.get_full_name()

    def email(self, obj):
        return obj.user.email


    list_display = [
        "full_name",
        "email",
        "phone_number",
        "address",
        "assigned_ward",
    ]


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    def ward(self, obj):
        return obj.polling_unit.ward
    list_display = [
        "agent",
        "ward",
        "polling_unit",
        "uploaded_at",
        "recorded_at",
        "pdp",
        "apc",
        "nnpp",
        "image",
    ]