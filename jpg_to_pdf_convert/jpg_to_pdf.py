import os
from PIL import Image


def convert_and_replace(file_path, source_dir, dest_dir):
    rel_path = os.path.relpath(file_path, source_dir)
    dest_path = os.path.join(dest_dir, rel_path)
    dest_root, dest_ext = os.path.splitext(dest_path)
    if dest_ext.lower() == '.pdf':
        os.makedirs(os.path.split(dest_root)[0], exist_ok=True)
        with Image.open(file_path) as img:
            img.convert('RGB').save(dest_path)
        os.remove(file_path)


def recursive_convert(dir_path, source_dir, dest_dir):
    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)
        if os.path.isdir(item_path):
            recursive_convert(item_path, source_dir, dest_dir)
        else:
            convert_and_replace(item_path, source_dir, dest_dir)


source_dir = 'D:\\SOY_100'
dest_dir = 'D:\\SOY_200'

recursive_convert(source_dir, source_dir, dest_dir)
