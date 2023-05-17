import os
import shutil
from PIL import Image

def convert_jpg_to_pdf(jpg_path, pdf_path):
    with Image.open(jpg_path) as img:
        if img.mode != "RGB":
            img = img.convert("RGB")
        img.save(pdf_path, "PDF", resolution=100.0)

def batch_convert_jpg_to_pdf(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for item in os.listdir(input_folder):
        item_path = os.path.join(input_folder, item)
        if os.path.isfile(item_path) and (item.endswith(".jpg") or item.endswith(".jpeg")):
            pdf_path = os.path.join(output_folder, f"{os.path.splitext(item)[0]}.pdf")
            convert_jpg_to_pdf(item_path, pdf_path)
        elif os.path.isdir(item_path):
            new_output_folder = os.path.join(output_folder, item)
            shutil.copytree(item_path, new_output_folder)
            batch_convert_jpg_to_pdf(item_path, new_output_folder)

input_folder = 'D://SOY_100'
output_folder = 'D://SOY_200'

batch_convert_jpg_to_pdf(input_folder, output_folder)