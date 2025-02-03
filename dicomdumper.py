import glob
import os
import argparse
from pydicom import dcmread
from pydicom.encaps import generate_pixel_data_frame


def process_file(filepath: str, extension:str):
    dataset = None
    try:
        dataset = dcmread(filepath)
    except Exception as err:
        print(f"Unexpected {err=}")
        return

    print(f"Patient's Name: {dataset.PatientName}")
    print(f"Modality: {dataset.Modality}")
    print(f"Study Date: {dataset.StudyDate}")
    print(f"Transfer syntax uid: {dataset.file_meta.TransferSyntaxUID}")
    print(f"Transfer syntax: {dataset.file_meta.TransferSyntaxUID.name}")

    # For now just assume mp4 for now so some kind of video player like VLC opens
    # and will read the header for the file.
    output_filename = os.path.splitext(filepath)[0] + extension
    with open(output_filename, 'wb') as f:
        f.write(next(generate_pixel_data_frame(dataset.PixelData)))


parser = argparse.ArgumentParser(description="Dicom extractor")
parser.add_argument('--file', type=str, help="Path to single dicom file")
parser.add_argument('--directory', type=str, help="Path to a directory with multiple dicom files")
parser.add_argument('--pattern', type=str, default='*.dcm', help="Pattern to match when searching files (default *.dcm)")
parser.add_argument('--extension', type=str, default='.mp4', help="Extension to set for the extracted file (default .mp4)")
args = parser.parse_args()
if args.file:
    print(f'Processing file: {args.file}')
    process_file(os.path.abspath(args.file), args.extension)

if args.directory:
    dcm_files = glob.glob(os.path.join(args.directory, args.pattern))
    for dcm_file in dcm_files:
        print(f'Processing file: {dcm_file}')
        process_file(os.path.abspath(dcm_file), args.extension)
