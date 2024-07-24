import os
import tkinter as tk
from tkinter import filedialog
import logging

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def select_folder():
    """Use tkinter to let the user select a folder and return the selected path."""
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    folder_selected = filedialog.askdirectory(title="Select Folder")
    if folder_selected:
        return folder_selected
    else:
        return None

def copy_folder_structure(src):
    """Copy the folder structure from src to its parent directory without copying the files."""
    if not src:
        logging.error("No source folder selected.")
        return

    parent_dir = os.path.dirname(src)
    folder_name = os.path.basename(src)
    dst = os.path.join(parent_dir, f"{folder_name}_copy")

    if not os.path.exists(dst):
        os.makedirs(dst)
    
    for dirpath, dirnames, filenames in os.walk(src):
        structure = os.path.join(dst, os.path.relpath(dirpath, src))
        try:
            if not os.path.isdir(structure):
                os.makedirs(structure)
        except Exception as e:
            logging.error(f"Error creating directory {structure}: {e}")

def main():
    setup_logging()
    src_folder = select_folder()
    
    if not src_folder:
        logging.info("No folder selected.")
        return

    if not os.path.isdir(src_folder):
        logging.info("The provided path is not a valid directory.")
        return
    
    copy_folder_structure(src_folder)
    logging.info(f"The folder structure of '{src_folder}' has been copied to its parent directory without the files.")

if __name__ == "__main__":
    main()
