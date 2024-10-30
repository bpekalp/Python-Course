from fpdf import FPDF

pdf = FPDF(orientation="portrait", unit="mm", format="A4")

pdf.add_page()
pdf.output("output.pdf")
