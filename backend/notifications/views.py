from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import ReportHistorySerializer
from .models import ReportDelivery
import logging
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .email import send_report_email
from django.contrib.auth.models import User
from datetime import date

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

@csrf_exempt
@require_http_methods(["POST"])
def test_email(request):
    try:
        test_user, created = User.objects.get_or_create(
            username='test_user',
            defaults={
                'email': 'test@example.com',
                'is_active': True
            }
        )
        
        logger.info(f"Sending test email to {test_user.email}")
        send_report_email(test_user, date.today(), 'HTML')
        
        return JsonResponse({
            'status': 'success',
            'message': f'Test email sent to {test_user.email}'
        })
    except Exception as e:
        logger.error(f"Failed to send test email: {str(e)}", exc_info=True)
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500) 