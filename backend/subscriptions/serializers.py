from rest_framework import serializers
from .models import Subscription

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'start_date', 'end_date', 'report_format', 'last_send_date', 'created_at']
        read_only_fields = ['id', 'last_send_date', 'created_at']
        
    def validate(self, attrs):
        start_date = attrs.get('start_date')
        end_date = attrs.get('end_date')
        if start_date and end_date and start_date > end_date:
            raise serializers.ValidationError("End date cannot be before start date.")
        return attrs