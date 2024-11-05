from django.shortcuts import render
from django.http import JsonResponse
from dashboard.models import DataEntry

def dashboard_view(request):
    data = DataEntry.objects.all()  # Filter and aggregate as needed
    context = {
        'data': data,
    }
    return render(request, 'dashboard/dashboard.html', context)

def get_data_api(request):
    country = request.GET.get('country', '')
    region = request.GET.get('region', '')

    data = DataEntry.objects.all()

    if country:
        data = data.filter(country=country)
    if region:
        data = data.filter(region=region)

    data = list(data.values())
    return JsonResponse(data, safe=False)
