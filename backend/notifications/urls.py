from django.urls import path
from .views import ReportHistoryView
from . import views

urlpatterns = [
    path('reports/history/', ReportHistoryView.as_view(), name='report-history'),
    path('test-email/', views.test_email, name='test_email'),
] 