from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class ReportDelivery(models.Model):
    FORMAT_CHOICES = [
        ('PDF', 'PDF'),
        ('HTML', 'HTML'),
        ('BOTH', 'Both'),
    ]

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('SENT', 'Sent'),
        ('FAILED', 'Failed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='report_deliveries')
    report_date = models.DateField()
    sent_at = models.DateTimeField(auto_now_add=True)
    report_format = models.CharField(max_length=5, choices=FORMAT_CHOICES, default='BOTH')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    error_message = models.TextField(blank=True, null=True)
    pdf_path = models.CharField(max_length=255, null=True, blank=True)
    html_content = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-sent_at']
        verbose_name = "Report Delivery"
        verbose_name_plural = "Report Deliveries"
        indexes = [
            models.Index(fields=['user', 'report_date']),
            models.Index(fields=['status']),
        ]

    def __str__(self):
        return f"{self.user.email} | {self.report_date} | {self.status}"
