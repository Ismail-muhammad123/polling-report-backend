from rest_framework.permissions import BasePermission

from reports.models import AgentProfile

class IsAnAgent(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return bool(request.user and AgentProfile.objects.filter(user=request.user).exists())