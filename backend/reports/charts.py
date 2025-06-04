import matplotlib.pyplot as plt
import os

def generate_report_chart(report_data, output_path = "report.pdf"):
    categories = ['Active Users', 'New Users', 'Total Users', 'Sessions', 'Page Views']
    values = [
        report_data['active_users'],
        report_data['new_users'],
        report_data['total_users'],
        report_data['sessions'],
        report_data['page_views']
    ]

    plt.figure(figsize=(10, 6))
    plt.bar(categories, values, color=['blue', 'green', 'orange', 'red', 'purple'])
    plt.title(f"Report for {report_data['date']}")
    plt.xlabel('Categories')
    plt.ylabel('Count')
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)
    plt.close()