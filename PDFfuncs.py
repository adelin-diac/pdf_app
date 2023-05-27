from PIL import Image
from PyPDF2 import PdfFileMerger
import os

def convert_and_save(text):
    print("Converting file(s)...")
    Paths = text.split("\n")
        # CLEANING UP THE PATH FILE SO CODE CAN UNDERSTAND & SAVING CONVERTED FILES
    for path in Paths:
        path = path.replace("\\", "/")
        path = path.strip("\"")
        try:
            image_1 = Image.open(path)
            im_1 = image_1.convert('RGB')
            
            fileName = getFileName(path)

            savePath = "conversions/"
            if not os.path.isdir(savePath):
                os.mkdir(savePath)
            
            im_1.save(savePath + fileName + "_converted.pdf")
        except FileNotFoundError:
            print("Path not found, ensure it is typed correctly")
            return
    print("Conversion complete")

def mergePDFs(text):
    print("Merging files...")
    Paths = text.split("\n")
    fileName = getFileName(Paths[0])
        # CLEANING UP THE PATH FILE SO CODE CAN UNDERSTAND & SAVING CONVERTED FILES
    merger = PdfFileMerger()
    for path in Paths:
        path = path.replace("\\", "/")
        path = path.strip("\"")
        try:
            merger.append(path)
        except FileNotFoundError:
            print("Path not found, ensure it is typed correctly")
            return
    savePath= "merges/"
    if not os.path.isdir(savePath):
        os.mkdir(savePath)
    merger.write(savePath + fileName + "_merged.pdf")
    merger.close()
    print("Merging complete")

def getFileName(path):
    path = path.replace('.', '/')
    splitPath = path.split('/')
    return splitPath[-2]
    