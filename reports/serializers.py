from dataclasses import field, fields
from rest_framework.serializers import ModelSerializer
from .models import AgentProfile, Ward, PollingUnit, Report
from rest_framework.serializers import StringRelatedField
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        field = ["first_name", "last_name", "email"]

class AgentsSerialiser(ModelSerializer):
    assigned_ward = StringRelatedField()
    user = UserSerializer()
    class Meta:
        model = AgentProfile
        fields = [
            "user",
            "phone_number",
            "address",
            "assigned_ward",
        ]



class WardSerializer(ModelSerializer):
    agents = AgentsSerialiser(many=True)
    class Meta:
        model = Ward
        fields = [
            "local_government",
            "name",
            "agents",
            "added_at",
        ]


class PollingUnitSerialiser(ModelSerializer):
    ward = StringRelatedField()
    class Meta:
        fields =[
        "name",
        "ward",
        "added_at",
        ]
        model = PollingUnit

class ReportSerialiser(ModelSerializer):
    agent = AgentsSerialiser()
    polling_unit = PollingUnitSerialiser()
    class Meta:
        model = Report
        fields = [
            "agent",
            "polling_unit",
            "uploaded_at",
            "recorded_at",
            "pdp",
            "apc",
            "nnpp",
            "image",
        ]


