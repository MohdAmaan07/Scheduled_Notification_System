from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Subscription(models.Model):
    FORMAT_CHOICE = [
        ('PDF', 'PDF Only'),
        ('HTML', 'HTML Only'),
        ('BOTH', 'Both PDF and HTML'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    email = models.EmailField(unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    report_format = models.CharField(max_length=5, choices=FORMAT_CHOICE, default='BOTH')
    last_send_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email}: {self.start_date} → {self.end_date}"

    class Meta:
        verbose_name = "Subscription"
        verbose_name_plural = "Subscriptions"
        constraints = [
            models.CheckConstraint(
                check=models.Q(start_date__lte=models.F('end_date')),
                name='start_date_before_end_date'
            ),
        ]
        ordering = ['-created_at']
