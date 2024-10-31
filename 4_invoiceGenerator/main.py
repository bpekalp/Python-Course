import pandas as pd
import glob as gl
import datetime
from fpdf import FPDF
import os

dataFolder = "4_invoiceGenerator/datasource"
filePaths = gl.glob(f"{dataFolder}/*.xlsx")

for filePath in filePaths:
    df = pd.read_excel(filePath)
    # print(f"Data Frame: {df}\n")

    filePath = filePath.lstrip(f"{dataFolder}/").rstrip(".xlsx")
    # print(f"File Path: {filePath}\n")

    index, date = filePath.split("-")
    index = int(index)
    # print(f"Index: {index} - Date: {date}\n")

    fIndex = f"Invoice ID: {index}"
    # print(f"Formatted Index: {fIndex}\n")

    year, month, day = date.split(".")
    year, month, day = int(year), int(month), int(day)
    # print(f"Y-M-D: {year} {month} {day}\n")

    date = datetime.datetime(year, month, day)
    fDate = f"Date: {date.strftime("%b %d, %Y")}"
    # print(f"Formatted Date: {fDate}\n")

    pdf = FPDF(orientation="p", unit="mm", format="a4")
    pdf.add_page()

    size = 16
    pdf.set_font(family="Helvetica", style="b", size=size)
    pdf.cell(w=0, h=size/2.0, txt=fIndex, ln=1)
    pdf.cell(w=0, h=size/2.0, txt=fDate, ln=1)

    dfTuple = tuple(map(tuple, df.values))
    # print(f"Tuple: {dfTuple}\n")

    if not os.path.exists("PDFs/"):
        os.makedirs("PDFs/")

    pdf.output(f"PDFs/{index}.pdf")

    # print("End of iteration.\n")
