import os
import subprocess

def run_pdf_metadata_updater():
    """
    Run the PDF Metadata Updater script located in the 'src' folder.

    This script changes the working directory to the 'src' folder and executes the
    PDF-Metadata-Updater.py script.

    Usage:
    1. Ensure that the 'src' folder contains the PDF-Metadata-Updater.py script.
    2. Run this start.py script from the root folder of the project.

    Dependencies:
    - subprocess

    Returns:
    None
    """

    # Navigate to the src folder
    src_folder = os.path.join(os.path.dirname(__file__), 'src')
    os.chdir(src_folder)

    # Run PDF-Metadata-Updater.py script
    subprocess.run(['python', 'PDF-Metadata-Updater.py'])

if __name__ == "__main__":
    run_pdf_metadata_updater()