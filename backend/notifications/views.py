from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import ReportHistorySerializer
from .models import ReportDelivery
import logging

logger = logging.getLogger('notifications')

class ReportHistoryView(ListAPIView):
    serializer_class = ReportHistorySerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        logger.info(f"Fetching report history for user: {user.email}")
        queryset = ReportDelivery.objects.filter(user=user)
        logger.info(f"Found {queryset.count()} reports for user {user.email}")
        return queryset 