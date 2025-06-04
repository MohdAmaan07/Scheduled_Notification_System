import random
from datetime import date

def generate_mock_report(report_date: date) -> dict:
    return {
        "date": report_date.isoformat(),
        "active_users": random.randint(100, 1000),
        "new_users": random.randint(10, 100),
        "total_users": random.randint(1000, 5000),
        "sessions": random.randint(500, 2000),
        "page_views": random.randint(2000, 10000),
    }