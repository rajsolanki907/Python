# Desktop Cleaner

A Python utility to automatically organize your Downloads folder by file type.

## Overview

`desktop_cleaner.py` scans a directory and organizes files into categorized subfolders based on their file extensions. It's designed to keep your Downloads folder clean and organized automatically.

## Features

- ✅ Automatically categorizes files by type (Videos, Images, Documents, Applications, Archives)
- ✅ Creates category folders automatically
- ✅ Skips hidden files (`.DS_Store`, etc.) and directories
- ✅ Prevents overwriting duplicate files
- ✅ Handles unknown file types in an "Other" folder
- ✅ Safe to run multiple times

## Setup

### Prerequisites
- Python 3.6+
- No external dependencies (uses only Python standard library)

### Installation

1. Clone or download this repository
2. Navigate to the folder:
```bash
cd /Users/raj/WebstormProjects/Python
```

## Configuration

**Before running the script, you must set your Downloads path:**

Open `desktop_cleaner.py` and edit this line (around line 4):
```python
DOWNLOADS_DIR = "--DOWNLOADS_PATH_HERE--"
```

Replace it with your actual Downloads path:
```python
DOWNLOADS_DIR = "/Users/your_username/Downloads"
```

### Example paths:
- macOS: `/Users/your_username/Downloads`
- Linux: `/home/your_username/Downloads`
- Windows: `C:\Users\your_username\Downloads`

## Usage

Run the script:
```bash
python desktop_cleaner.py
```

## File Categories

The script organizes files into these categories:

| Category | Extensions |
|----------|-----------|
| **Videos** | `.mp4`, `.mov`, `.avi`, `.mkv`, `.flv` |
| **Images** | `.jpg`, `.jpeg`, `.png`, `.gif`, `.tiff` |
| **Documents** | `.pdf`, `.docx`, `.doc`, `.txt`, `.rtf`, `.xlsx`, `.csv`, `.xls` |
| **Applications** | `.exe`, `.dmg`, `.pkg` |
| **Archives** | `.zip`, `.rar`, `.7z` |
| **Other** | Any unrecognized file type |

## Example Output

```
--- Starting Scan of /Users/raj/Downloads ---
Created folder: Videos
Created folder: Images
Created folder: Documents
Created folder: Applications
Created folder: Archives
  MOVED: vacation.mp4 -> Videos
  MOVED: screenshot.png -> Images
  MOVED: report.pdf -> Documents
  MOVED: installer.dmg -> Applications
  MOVED: archive.zip -> Archives

--- Cleaning Complete: 5 files moved. ---
```

## How It Works

1. **Scans the directory** and lists all files
2. **Creates category folders** if they don't exist
3. **Identifies file type** by checking the file extension
4. **Moves the file** to the appropriate category folder
5. **Skips duplicates** if a file with the same name already exists in the destination
6. **Reports progress** showing which files were moved

## Safety Features

- ❌ Does **NOT** overwrite existing files (skips duplicates)
- ❌ Does **NOT** move hidden files (e.g., `.DS_Store`, `.gitignore`)
- ❌ Does **NOT** move directories (only files)
- ❌ Does **NOT** move itself if located in the target folder
- ⚠️ **Always backs up important files before running!**

## Customization

To add or modify file categories, edit the `FILE_TYPES` dictionary in the script:

```python
FILE_TYPES = {
    "Videos": ['.mp4', '.mov', '.avi', '.mkv', '.flv'],
    "Images": ['.jpg', '.jpeg', '.png', '.gif', '.tiff'],
    # Add your own categories here:
    "MyCategory": ['.ext1', '.ext2'],
}
```

## Requirements

- Python 3.6 or higher
- Read/write permissions for the target directory

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Script doesn't move any files | Check that `DOWNLOADS_DIR` is set to a valid path |
| `Permission denied` error | Ensure you have write permissions for the Downloads folder |
| Files are not organized | Make sure file extensions are in lowercase (the script converts them) |
| Script moved files I didn't want moved | Edit `FILE_TYPES` to remove unwanted extensions |

## Warnings

⚠️ **Important:**
- **Always backup important files** before running this script
- Test on a small folder first before using on your main Downloads
- The script moves files permanently (not to trash)
- Hidden files and system files are automatically skipped for safety

## Running Safely (First Time)

1. **Test on a test folder:**
   - Create a test folder with sample files
   - Update `DOWNLOADS_DIR` to point to the test folder
   - Run the script to verify behavior
   
2. **Then use on actual Downloads:**
   - Backup your Downloads folder
   - Update `DOWNLOADS_DIR` to your real path
   - Run the script

## Example: Before and After

**Before:**
```
Downloads/
├── vacation.mp4
├── screenshot.png
├── report.pdf
├── installer.dmg
├── data.zip
└── notes.txt
```

**After:**
```
Downloads/
├── Videos/
│   └── vacation.mp4
├── Images/
│   └── screenshot.png
├── Documents/
│   ├── report.pdf
│   └── notes.txt
├── Applications/
│   └── installer.dmg
├── Archives/
│   └── data.zip
└── Other/
```

## License

Free to use and modify for personal use.

## Questions or Issues?

- Review the script comments for detailed explanations
- Check the Troubleshooting section above
- Ensure `DOWNLOADS_DIR` is correctly set before running
