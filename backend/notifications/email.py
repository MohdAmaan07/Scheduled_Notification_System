from django.core.mail import send_mail
from django.conf import settings
from reports.report_builder import build_report
import logging
import os

logger = logging.getLogger('notifications')

def send_report_email(user, report_date, report_format):
    try:
        logger.info(f"Building report for {user.email} for date {report_date}")
        report = build_report(report_date)
        
        subject = f'Daily Report - {report_date}'
        message = 'Please find your daily report attached.'
        
        if report.get('html_content'):
            message = report['html_content']
        
        logger.info(f"Sending {report_format} report to {user.email}")
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            html_message=message if report_format == 'html' else None,
            fail_silently=False,
        )
        logger.info(f"Email sent successfully to {user.email}")
        
        if report_format.upper() in ['PDF', 'BOTH'] and os.path.exists(report['pdf_path']):
            with open(report['pdf_path'], 'rb') as pdf_file:
                email.attach(
                    filename=f"report_{report_date.isoformat()}.pdf",
                    content=pdf_file.read(),
                    mimetype='application/pdf'
                )
        
        if report_format.upper() in ['HTML', 'BOTH']:
            email.content_subtype = 'html'
        
        email.send(fail_silently=False)
        
    except Exception as e:
        logger.error(f"Failed to send email to {user.email}: {str(e)}", exc_info=True)
        raise
