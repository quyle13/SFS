from IACS_CSMS.models import Asset,Application,Zone,Conduit,Risk,CounterMeasure
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from IACS_CSMS import Chart

def risk_view(request):
	context = {
        'bar_chart': Chart.BarChart(),
         'pie_chart': Chart.PieChart(),
         'line_chart': Chart.LineChart(),
       }
	return render(request, 'change_list_graph.html', context)
