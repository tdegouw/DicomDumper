import os
import argparse
from pydicom import dcmread
from pydicom.encaps import generate_pixel_data_frame

parser = argparse.ArgumentParser(description="Dump de video vanuit een DCM file.")
parser.add_argument('input_file', type=str, help="Relatief pad naar de dicom file")

args = parser.parse_args()
dicom_file_absolute = os.path.abspath(args.input_file)
dataset = dcmread(dicom_file_absolute)

print(f"Patient's Name: {dataset.PatientName}")
print(f"Modality: {dataset.Modality}")
print(f"Study Date: {dataset.StudyDate}")
print(f"Transfer syntax uid: {dataset.file_meta.TransferSyntaxUID}")
print(f"Transfer syntax: {dataset.file_meta.TransferSyntaxUID.name}")

# Just assume mp4 for now so some kind of video player like VLC opens
# and will read the header for the file
output_filename = os.path.splitext(dicom_file_absolute)[0] + ".mp4"
with open(output_filename , 'wb') as f:
    f.write(next(generate_pixel_data_frame(dataset.PixelData)))