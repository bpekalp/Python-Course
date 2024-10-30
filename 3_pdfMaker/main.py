from fpdf import FPDF
import pandas as pd

topics = pd.read_csv("3_pdfMaker/datasource/topics.csv")

pdf = FPDF(orientation="portrait", unit="mm", format="A4")

size = 12

lineX1 = 10
lineX2 = 200
lineY = 2.0 * size

for i, topic in topics.iterrows():
    title = topic["Topic"]
    pages = topic["Pages"]

    pdf.add_page()

    pdf.set_font(family="Times", size=2.0 * size)
    pdf.cell(w=0, h=size, txt=title, border=0, ln=1)

    pdf.line(lineX1, lineY, lineX2, lineY)

    for j in range(int(pages) - 1):
        pdf.add_page()

pdf.output("output.pdf")
