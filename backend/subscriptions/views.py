from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import SubscriptionSerializer
from .models import Subscription
from django.contrib.auth import get_user_model
from datetime import date

# Create your views here.
User = get_user_model()

class SubscriptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        user = self.request.user
        if user.is_anonymous:
            user = User.objects.first()
        obj, created = Subscription.objects.get_or_create(
            user=user,
            defaults={
                'start_date': date.today(),
                'end_date': date.today(),
            }
        )
        return obj