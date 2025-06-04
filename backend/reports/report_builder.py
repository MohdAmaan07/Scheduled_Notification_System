from django.template.loader import render_to_string
from .utils import generate_mock_report
from .charts import generate_report_chart
from .pdf import build_pdf
import os
import base64
from pathlib import Path

def build_report(report_date):
    report_data = generate_mock_report(report_date)
        
    chart_path = Path(f"reports/charts/report_{report_date.isoformat()}.png")
    pdf_path = Path(f"reports/pdf/report_{report_date.isoformat()}.pdf")

    ensure_path(chart_path)
    ensure_path(pdf_path)
        
    generate_report_chart(report_data, chart_path)

    chart_data_uri = get_base64_image(chart_path)
    html_content = render_to_string('reports/report_template.html', {
        'report_data': report_data,
        'chart_path': chart_data_uri
    })
  
    build_pdf(report_data, chart_data_uri, pdf_path)

    return {
        "report_data": report_data,
        "html_content": html_content,
        "chart_path": str(chart_path),
        "pdf_path": str(pdf_path)
    }

def ensure_path(path):
    os.makedirs(Path(path).parent, exist_ok=True)

def get_base64_image(img_path):
    with open(img_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("utf-8")
    return f"data:image/png;base64,{encoded}"
