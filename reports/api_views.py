from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404
from reports.models import AgentProfile, PollingUnit, Report, Ward
from reports.serializers import AgentsSerialiser, ReportSerialiser, WardSerializer
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.views import APIView
import datetime
from .permissions import IsAnAgent



# get all wards
class WardList(APIView):
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def get(self, request, format=None):
        snippets = Ward.objects.all()
        serializer = WardSerializer(snippets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



# get list of all agents
class AgentList(APIView):
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def get(self, request, format=None):
        snippets = AgentProfile.objects.all()
        serializer = AgentsSerialiser(snippets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



# get polling units within agent's assigned ward
class AgentPollingUnitsList(APIView):
    permission_classes = [permissions.IsAuthenticated, IsAnAgent]

    def get(self, request, format=None):
        ward_id = request.GET.get("ward_id", None)

        if ward_id is not None:
            ward = get_object_or_404(Ward, id=ward_id)

            units = PollingUnit.objects.filter(ward=ward)

            serialized_units = WardSerializer(instance=units, many=True)

            return Response(serialized_units.data, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)



class AllPollingUnitsList(APIView):
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def get(self, request, format=None):
        units = PollingUnit.objects.all()

        serialized_units = WardSerializer(instance=units, many=True)

        return Response(serialized_units.data, status=status.HTTP_200_OK)    


# get reports
class ReportsList(APIView):
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def get(self, request, format=None):
        reports = Report.objects.all()
        serialized_reports = ReportSerialiser(instance=reports, many=True)

        return Response(serialized_reports.data, status=status.HTTP_200_OK)  





# add report
class AddReportView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsAnAgent]

    def post(self, request, format=None):
        agent = AgentProfile.objects.get(user=request.user)

        data = request.data
        
        unit_id = data.get('polling_unit')
        polling_unit = PollingUnit.objects.get(id=unit_id)

        pdp = data.get('pdp')
        apc = data.get('apc')
        nnpp = data.get('nnpp')

        time_recorded = data.get('time_recorded')

        image = request.FILES.get('image')

        report = Report(
            agent = agent,
            polling_unit = polling_unit,
            recorded_at = datetime.datetime.fromtimestamp(time_recorded),
            pdp = pdp,
            apc = apc,
            nnpp = nnpp,
            image = image,
        )

        report.save()

        return Response(status=status.HTTP_201_CREATED) 


    

