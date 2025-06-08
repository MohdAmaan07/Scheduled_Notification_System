from django.urls import path
from .views import SubscriptionDetailView

urlpatterns = [
    path('', SubscriptionDetailView.as_view(), name='subscription-list'),
    path('<int:pk>/', SubscriptionDetailView.as_view(), name='subscription-detail'),
]
