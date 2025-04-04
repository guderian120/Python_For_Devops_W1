from django.shortcuts import render
from .models import SystemHealth
from rest_framework.response import Response
from rest_framework.decorators import api_view
import psutil

@api_view(['POST'])
def get_metrics(request):
    data = request.data
    md = SystemHealth()
    md.cpu_usage = data['CPU']
    md.memory_usage = data['MEMORY']
    md.disk_usage = data['DISK']
    md.save()
    return Response({"ok":"okay"})

@api_view(['GET'])
def display_dashboard(request):
    logs = SystemHealth.objects.all().order_by('-timestamp')[:10]
    data = [{"timestamp": log.timestamp, "cpu": log.cpu_usage, "memory": log.memory_usage, "disk": log.disk_usage} for log in logs]
    return Response(data)

