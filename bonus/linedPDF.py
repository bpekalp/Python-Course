from fpdf import FPDF
import pandas as pd


def footer(_pdf, _topic):
    _size = 8
    _pdf.set_y(-1.5 * _size)
    _pdf.set_font("Arial", "I", _size)
    _pdf.set_text_color(64, 64, 64)
    _pdf.cell(
        w=0,
        h=_size,
        txt=f"Page {_pdf.page_no()}, {_topic["Topic"]}",
        border=0,
        ln=0,
        align="R",
    )


def drawLines(_pdf, _lineX1, _lineX2, _lineY, _cursorY):
    for i in range(int((297 - _cursorY) / _lineY)):
        _pdf.line(_lineX1, _cursorY, _lineX2, _cursorY)
        _cursorY += 10


topics = pd.read_csv("3_pdfMaker/datasource/topics.csv")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

size = 12

lineX1 = 10
lineX2 = 200
lineY = 10
cursorY = 10 + size

for i, topic in topics.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", size=size)
    pdf.cell(w=0, h=size, txt=topic["Topic"], border=0, ln=1)

    footer(pdf, topic)

    drawLines(pdf, lineX1, lineX2, lineY, cursorY)

    for j in range(int(topic["Pages"])):
        pdf.add_page()
        footer(pdf, topic)
        drawLines(pdf, lineX1, lineX2, lineY, cursorY)


pdf.output("linedPDF.pdf")
