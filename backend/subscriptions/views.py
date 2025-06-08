from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import SubscriptionSerializer
from .models import Subscription
from django.contrib.auth import get_user_model
from datetime import date

# Create your views here.
User = get_user_model()

class SubscriptionDetailView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            user = User.objects.first()
        return Subscription.objects.filter(user=user)
    
    def perform_create(self, serializer):
        user = self.request.user
        if user.is_anonymous:
            user = User.objects.first()
        serializer.save(user=user)