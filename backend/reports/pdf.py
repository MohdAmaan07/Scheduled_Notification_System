from weasyprint import HTML
from django.template.loader import render_to_string

def build_pdf(report_data, chart_path, output_path = 'report.pdf'):
    html_string = render_to_string('reports/report_template.html', {
        'report_data': report_data,
        'chart_path': chart_path
    })

    HTML(string=html_string).write_pdf(output_path)