from celery import shared_task
from datetime import date
from .models import ReportDelivery
from .email import send_report_email
from subscriptions.models import Subscription
from reports.report_builder import build_report
import logging

logger = logging.getLogger('notifications')

@shared_task
def send_daily_updates():
    today = date.today()
    logger.info(f"Starting daily updates for {today}")
    
    active_subscriptions = Subscription.objects.filter(
        start_date__lte=today,
        end_date__gte=today,
    )
    logger.info(f"Found {active_subscriptions.count()} active subscriptions")
    
    for subscription in active_subscriptions:
        logger.info(f"Processing subscription for user: {subscription.user.email}")
        if not ReportDelivery.objects.filter(
            user=subscription.user,
            report_date=today
        ).exists():
            try:
                logger.info("Generating report...")
                report = build_report(today)
                
                logger.info("Sending email...")
                send_report_email(subscription.user, today, subscription.report_format)
                
                logger.info("Creating delivery record...")
                delivery = ReportDelivery.objects.create(
                    user=subscription.user,
                    report_date=today,
                    report_format=subscription.report_format,
                    status='SENT',
                    pdf_path=report['pdf_path'],
                    html_content=report['html_content']
                )
                logger.info(f"Created delivery record: {delivery.id}")
                
                subscription.last_send_date = today
                subscription.save(update_fields=['last_send_date'])
                logger.info("Updated subscription last send date")
                
            except Exception as e:
                logger.error(f"Error occurred: {str(e)}", exc_info=True)
                ReportDelivery.objects.create(
                    user=subscription.user,
                    report_date=today,
                    report_format=subscription.report_format,
                    status='FAILED',
                    error_message=str(e)
                )
        else:
            logger.info("Report already sent for today")
    