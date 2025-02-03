# DicomDumper
Simple script to dump the video out of a dicom file

## Usage

Install requirements before usage
```
python -m pip install -r requirements.txt
```

And run the script either on a single file or a list of files.

For help on parameters use -h
```
python dicomdumper.py -h
```

To run against a directory use the --directory
```
python dicomdumper.py --directory '/path/to/dcmfiles'
```

To run against a single file use the --file parameter
```
python dicomdumper.py --file '/path/to/file.dcm'
```