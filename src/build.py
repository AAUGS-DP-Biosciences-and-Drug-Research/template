import markdown
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
import weasyprint

# Convert README.md to HTML
with open("README.md", "r", encoding="utf-8") as f:
    md_content = f.read()
html_content = markdown.markdown(md_content, extensions=["extra", "tables"])

# Load template
env = Environment(loader=FileSystemLoader("src/templates"))
template = env.get_template("template.html")
rendered_html = template.render(content=html_content)

# Write HTML
Path("public").mkdir(exist_ok=True)
html_path = Path("public/index.html")
html_path.write_text(rendered_html, encoding="utf-8")

# Export PDF
pdf_path = Path("public/Document.pdf")
weasyprint.HTML(string=rendered_html).write_pdf(pdf_path)
