# File Organizer Using Packages and Modules

A Python program that organizes files into folders
based on their file extensions.

## Example

photo.jpg -> Images/

notes.txt -> Text/

report.pdf -> Documents/

data.csv -> Data/

## Features

- Detect file type
- Automatically create destination folders
- Move files safely
- Handle duplicate filenames
- Handle missing files
- Handle permission errors
- Handle unsupported file types
- Custom UnsupportedFileError
- Log successful operations
- Log failed operations

## Project Structure

file-organizer-using-packages-and-modules/

    file_organizer/
        __init__.py
        detector.py
        mover.py
        logger.py
        exceptions.py

    test_files/

    main.py
    README.md

## Supported Extensions

### Images

.jpg  
.jpeg  
.png  
.gif

### Text

.txt

### Documents

.pdf  
.doc  
.docx

### Data

.csv  
.xlsx

## Run

```bash
python main.py