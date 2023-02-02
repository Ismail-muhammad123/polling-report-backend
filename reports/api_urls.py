from django.urls import path
from .api_views import *


urlpatterns = [
    path('wards', WardList.as_view(), name='list_wards'),                           # GET
    path('units', AllPollingUnitsList, name='list_all_units'),                      # GET
    path('agent-wards', AgentPollingUnitsList.as_view(), name='get_agent_units'),   # GET
    path('agents', AgentList.as_view(), name='list_agents'),                        # GET
    path('reports', ReportsList.as_view(), name='list_reports'),                    # GET
    path('reports/new', AddReportView.as_view(), name='add_report'),                # POST
]