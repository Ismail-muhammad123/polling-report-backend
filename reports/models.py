from django.db import models
from django.contrib.auth.models import User


class Ward(models.Model):
    local_government = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    added_at = models.DateTimeField(auto_now_add=True)


class PollingUnit(models.Model):
    name = models.CharField(max_length=200)
    ward = models.ForeignKey(Ward, on_delete=models.SET_NULL, null=True, related_name="polling_units")
    added_at = models.DateTimeField(auto_now_add=True)


class AgentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    assigned_ward = models.ForeignKey(Ward, on_delete=models.SET_NULL, null=True, related_name="agents")


class Report(models.Model):
    agent = models.ForeignKey(AgentProfile, on_delete=models.SET_NULL, null=True, related_name="reports")
    polling_unit = models.ForeignKey(PollingUnit, on_delete=models.CASCADE, related_name="reports")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    recorded_at = models.DateTimeField()
    pdp =  models.PositiveIntegerField(default=0)
    apc = models.PositiveIntegerField(default=0)
    nnpp = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="report_images")