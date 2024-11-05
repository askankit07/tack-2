from django.urls import path
from .views import get_data_api, dashboard_view  # Import your view functions

urlpatterns = [
    path('get-data-api/', get_data_api, name='get_data_api'),
    path('', dashboard_view, name='dashboard_view'),  # Optional: Main dashboard page
]
