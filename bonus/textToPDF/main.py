from fpdf import FPDF
import glob
import os

datas = "bonus/textToPDF/datas"
fileNames = glob.glob(f"{datas}/*.txt")

pdf = FPDF(orientation="p", unit="mm", format="a4")

for fileName in fileNames:
    with open(fileName, "r") as file:
        content = file.read()

    title = str(os.path.splitext(os.path.basename(fileName))[0]).title()

    pdf.add_page()

    size = 16
    pdf.set_font(family="Times", style="b", size=size)
    pdf.cell(w=0, h=size, txt=title, ln=1)

    size = 12
    pdf.set_font(family="Times", size=size)
    pdf.multi_cell(w=0, h=size / 2.0, txt=content)

if not os.path.exists("PDFs/"):
    os.makedirs("PDFs/")

pdf.output(f"PDFs/textTo.pdf")
