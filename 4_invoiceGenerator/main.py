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

    filePath = os.path.splitext(os.path.basename(filePath))[0]
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
    pdf.cell(w=0, h=size/1.5, txt=fIndex, ln=1)
    pdf.cell(w=0, h=size/1.5, txt=fDate, ln=1)

    size = 12
    pdf.set_font(family="Helvetica", style="b", size=size)
    pdf.cell(w=24, h=size/1.5, border=1, txt="Product ID")
    pdf.cell(w=48, h=size/1.5, border=1, txt="Product Name")
    pdf.cell(w=48, h=size/1.5, border=1, txt="Purchased Amount")
    pdf.cell(w=36, h=size/1.5, border=1, txt="Price Per Unit")
    pdf.cell(w=24, h=size/1.5, border=1, txt="Total Price", ln=1)

    size = 10
    pdf.set_font(family="Helvetica", size=size)
    for i, row in df.iterrows():
        pdf.cell(w=24, h=size/1.5, border=1, txt=str(row["product_id"]))
        pdf.cell(w=48, h=size/1.5, border=1, txt=str(row["product_name"]))
        pdf.cell(w=48, h=size/1.5, border=1, txt=str(row["amount_purchased"]))
        pdf.cell(w=36, h=size/1.5, border=1, txt=str(row["price_per_unit"]))
        pdf.cell(w=24, h=size/1.5, border=1, txt=str(row["total_price"]), ln=1)

    totalPrice = df["total_price"].sum()

    size = 12
    pdf.set_font(family="Helvetica", size=size)
    pdf.cell(w=24, h=size/1.5)
    pdf.cell(w=48, h=size/1.5)
    pdf.cell(w=48, h=size/1.5)

    pdf.set_font(family="Helvetica", style="b", size=size)
    pdf.cell(w=36, h=size/1.5, border=1, txt="Total")

    pdf.set_font(family="Helvetica", size=size)
    pdf.cell(w=24, h=size/1.5, border=1, txt=str(totalPrice), ln=1)

    pdf.cell(w=0, h=size, border=0,
             txt=f"The total due amount is {totalPrice}$", ln=1)
    pdf.image("4_invoiceGenerator/datasource/pythonhow.png", w=12)

    if not os.path.exists("PDFs/"):
        os.makedirs("PDFs/")

    pdf.output(f"PDFs/{index}.pdf")

    # print("End of iteration.\n")
