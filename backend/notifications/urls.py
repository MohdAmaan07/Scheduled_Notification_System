from django.urls import path
from .views import ReportHistoryView

urlpatterns = [
    path('reports/history/', ReportHistoryView.as_view(), name='report-history'),
] 