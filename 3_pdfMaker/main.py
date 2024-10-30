from fpdf import FPDF
import pandas as pd


def addFooter(_pdf, _topic):
    _size = 8
    _pdf.set_y(-1.5 * _size)
    _pdf.set_font("Arial", "I", _size)
    _pdf.set_text_color(64, 64, 64)
    _pdf.cell(
        w=0,
        h=_size,
        txt=f"Page {pdf.page_no()}, {_topic["Topic"]}",
        border=0,
        ln=0,
        align="R",
    )


topics = pd.read_csv("3_pdfMaker/datasource/topics.csv")

pdf = FPDF(orientation="portrait", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

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
    addFooter(pdf, topic)

    for j in range(int(pages) - 1):
        pdf.add_page()

        addFooter(pdf, topic)

pdf.output("output.pdf")
