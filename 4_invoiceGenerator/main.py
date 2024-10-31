import pandas as pd
import glob as gl

dataFolder = "4_invoiceGenerator/datasource"
filePaths = gl.glob(f"{dataFolder}/*.xlsx")
fileInfos = []

for filePath in filePaths:
    df = pd.read_excel(filePath)

    filePath = filePath.lstrip(f"{dataFolder}/").rstrip(".xlsx")
    # print(f"File path: {filePath}")

    index, date = filePath.split("-")
    # print(f"Index: {index}, Date: {date}")

    year, month, day = date.split(".")
    # print(f"YYYY: {year}, MM: {month}, D: {day}")

    fileInfo = {
        "index": index,
        "year": year,
        "month": month,
        "day": day
    }
    # print(f"File Info: {fileInfo}")

    fileInfos.append(fileInfo)
    # print(f"File Info List: {fileInfos}")
