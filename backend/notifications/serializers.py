from rest_framework import serializers
from .models import ReportDelivery

class ReportHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportDelivery
        fields = [
            'id',
            'report_date',
            'sent_at',
            'report_format',
            'status',
            'error_message',
            'pdf_path',
            'html_content'
        ]
        read_only_fields = fields  
        