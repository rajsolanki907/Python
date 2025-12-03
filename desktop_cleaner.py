import os
import shutil

# --- Configuration ---
# !!! YOUR ACTUAL DOWNLOADS PATH !!!
DOWNLOADS_DIR = "/Users/raj/Downloads" 

# Define where files should go based on their extension
FILE_TYPES = {
    "Videos": ['.mp4', '.mov', '.avi', '.mkv', '.flv'],
    "Images": ['.jpg', '.jpeg', '.png', '.gif', '.tiff'],
    "Documents": ['.pdf', '.docx', '.doc', '.txt', '.rtf','.xlsx', '.csv', '.xls'],
    "Applications": ['.exe', '.dmg', '.pkg'],
    "Archives": ['.zip', '.rar', '.7z']
}

def create_folder_if_not_exists(path):
    """Creates a folder safely if it doesn't already exist."""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created folder: {path.split(os.path.sep)[-1]}")

def organize_files(source_dir, file_map):
    """Iterates through files and moves them to the correct directory."""
    
    print(f"\n--- Starting Scan of {source_dir} ---")
    
    # Pre-create all destination folders
    for folder_name in file_map:
        create_folder_if_not_exists(os.path.join(source_dir, folder_name))

    files_moved = 0
    
    for filename in os.listdir(source_dir):
        # *** FIX START: SKIP hidden files (like .DS_Store) and directories ***
        if filename.startswith('.') or os.path.isdir(os.path.join(source_dir, filename)):
            continue
        # *** FIX END ***

        # Skip the script itself if it is in the Downloads folder (unlikely but safe)
        if filename == os.path.basename(__file__):
             continue

        # Get the file extension (e.g., '.pdf')
        name, ext = os.path.splitext(filename)
        ext = ext.lower() # Standardize extension to lowercase
        
        # Check which folder it belongs to
        destination_folder = "Other"
        for folder, extensions in file_map.items():
            if ext in extensions:
                destination_folder = folder
                break
        
        # Define source and destination paths
        source_path = os.path.join(source_dir, filename)
        
        # IMPORTANT: Ensure the "Other" folder is created if needed
        if destination_folder == "Other":
            create_folder_if_not_exists(os.path.join(source_dir, "Other"))
            
        dest_folder_path = os.path.join(source_dir, destination_folder)
        dest_path = os.path.join(dest_folder_path, filename)
        
        # Move the file if the destination doesn't already have a file with that name
        if not os.path.exists(dest_path):
            shutil.move(source_path, dest_path)
            print(f"  MOVED: {filename} -> {destination_folder}")
            files_moved += 1
        
    print(f"\n--- Cleaning Complete: {files_moved} files moved. ---")

if __name__ == "__main__":
    organize_files(DOWNLOADS_DIR, FILE_TYPES)