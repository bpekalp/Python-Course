from fpdf import FPDF

pdf = FPDF(orientation="portrait", unit="mm", format="A4")

size = 12
pdf.set_font(family="Times", size=size)

pdf.add_page()
pdf.cell(w=0, h=size, txt="Hello World!", border=1, ln=1)

pdf.output("output.pdf")
