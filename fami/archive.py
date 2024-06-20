import os
import exifread
from datetime import datetime
import shutil

def run_archive(output_path):
    pwd = os.getcwd()
    # read all files in current directory
    files = os.listdir(pwd)

    for file in files:
        if not file.lower().endswith('.jpg'):
            continue
        with open(file, 'rb') as f:
            tags = exifread.process_file(f)
            date_str = str(tags.get('EXIF DateTimeOriginal'))
            if date_str:
                date_obj = datetime.strptime(date_str, '%Y:%m:%d %H:%M:%S')
                new_path = os.path.join(output_path, date_obj.strftime('%Y/%m/%d'))
                os.makedirs(new_path, exist_ok=True)
                shutil.move(file, os.path.join(new_path, file))
            else:
                print("could not extract date")
