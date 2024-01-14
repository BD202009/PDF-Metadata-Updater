"""
PDF Metadata Updater

This script updates the metadata of given PDF files.
It creates 'output', 'input', and 'config' folders in the root directory to store the processed files.

Author: Dennis Biehl

License:
MIT License

Dependencies:
- os
- PyPDF2
- configparser

Usage:
1. Ensure that PyPDF2 is installed using `pip install PyPDF2`.
2. Run the script to create 'output', 'input', and 'config' folders.
3. Place PDF files in the 'input' folder.
4. The script will merge each PDF's pages with its metadata and save the result in the 'output' folder.

Functions:
- create_folders(): Creates 'output', 'input', and 'config' folders if they don't exist and returns their paths.
- create_config(config_file, config): Creates a configuration file with a 'Metadata' section.
- update_config(config_file, config): Updates the configuration file with metadata values.
- process_pdf(original_file_path, output_folder, config): Merges the pages of a PDF with its metadata and saves the result.

Configuration:
- The 'output', 'input', and 'config' folders are created in the root directory.
- Metadata such as Producer and Creator are set during the merging process.

Version: 1.0.0
Release Date: 2024-01-14

Updates:
- 2024-01-14: Initial release.
"""

import os
import PyPDF2
from configparser import ConfigParser

def create_folders():
    """
    Creates 'output', 'input' and 'config' folders if they don't exist and returns their paths.

    Returns:
    - output_folder (str): Path to the 'output' folder.
    - input_folder (str): Path to the 'input' folder.
    - config_folder (str): Path to the 'input' folder.
    """
    
    # Output and input folder in the root directory
    output_folder = os.path.abspath(os.path.join(os.path.dirname(__file__),'..', 'output'))
    input_folder = os.path.abspath(os.path.join(os.path.dirname(__file__),'..', 'input'))
    config_folder = os.path.abspath(os.path.join(os.path.dirname(__file__),'..', 'config'))
        
    # Create the output and input folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    os.makedirs(input_folder, exist_ok=True)
    os.makedirs(config_folder, exist_ok=True)

    return output_folder, input_folder, config_folder

def create_config(config_file, config):
    """
    Creates a configuration file with a 'Metadata' section.

    Args:
    - config_file (str): Path to the configuration file.
    - config (ConfigParser): Configuration parser object.
    """
    
    config.add_section('Metadata')
    with open(config_file, 'w') as config_file:
        config.write(config_file)

def update_config(config_file, config):
    """
    Updates the configuration file with metadata values.

    Args:
    - config_file (str): Path to the configuration file.
    - config (ConfigParser): Configuration parser object.
    """
    
    config.read(config_file)

    producer = config.get('Metadata', 'Producer', fallback="")
    creator = config.get('Metadata', 'Creator', fallback="")
    
    if producer:
        print("Existing metadata value found in the config file:")
        print("Producer:", config.get('Metadata', 'Producer', fallback=""))
        confirm = input("Do you want to use this value? (y/n): ").lower()
        if confirm == 'n':
            producer = input("Enter the value for Producer: ")
            config.set('Metadata', 'Producer', producer)
            with open(config_file, 'w') as config_file:
                config.write(config_file)
            print("Metadata updated")
        else:
            print("Using existing metadata value.")
    else:
        producer = input("Enter the value for Producer: ")
        config.set('Metadata', 'Producer', producer)
        with open(config_file, 'w') as config_file:
            config.write(config_file)
        print("Metadata added to config")

    if creator:
        print("Existing metadata value found in the config file:")
        print("Creator:", config.get('Metadata', 'Creator', fallback=""))
        confirm = input("Do you want to use this value? (y/n): ").lower()
        if confirm == 'n':
            creator = input("Enter the value for Creator: ")
            config.set('Metadata', 'Creator', creator)
            with open(config_file, 'w') as config_file:
                config.write(config_file)
            print("Metadata updated")
        else:
            print("Using existing metadata value.")
    else:
        creator = input("Enter the value for Creator: ")
        config.set('Metadata', 'Creator', creator)
        with open(config_file, 'w') as config_file:
            config.write(config_file)
        print("Metadata added to config")

def process_pdf(original_file_path, output_folder, config):
    """
    Merges the pages of a PDF with its metadata and saves the result.

    Args:
    - original_file_path (str): Path to the original PDF file.
    - output_folder (str): Path to the 'output' folder.
    - config (ConfigParser): Configuration parser object.
    """
    
    # Create a PdfFileWriter object to manipulate original_file
    updater = PyPDF2.PdfWriter()

    with open(original_file_path, 'rb') as file:
        pdf2 = PyPDF2.PdfReader(file)

        # copy pages to updater
        for page_num in range(len(pdf2.pages)):
            page = pdf2.pages[page_num]
            page.merge_page(PyPDF2.PdfReader(original_file_path).pages[page_num])
            updater.add_page(page)
            
    # Get metadata values from the config file
    producer = config.get('Metadata', 'Producer', fallback="")
    creator = config.get('Metadata', 'Creator', fallback="")
    
    # Write metadata to the updater
    updater.add_metadata({
        "/Producer": producer,
        "/Creator": creator,
    })

    # Save the merged PDF as 'original_file_name.pdf' in the 'output' folder
    output_file_path = os.path.join(output_folder, os.path.basename(original_file_path))
    with open(output_file_path, 'wb') as output_file:
        updater.write(output_file)

if __name__ == "__main__":
    try:
        import PyPDF2
    except ImportError:
        print("PyPDF2 is not installed. Please install it using the following command:")
        print("pip install PyPDF2")
        exit()

    output_folder, input_folder, config_folder = create_folders()

    config = ConfigParser()
    
    # Check if the config file exists, create it if not
    config_file = os.path.join(config_folder, 'config.ini')
    if not os.path.isfile(config_file):
        create_config(config_file, config)

    update_config(config_file, config)
    
    # Iterate through all PDF files in the 'input' folder
    for original_file in os.listdir(input_folder):
        if original_file.endswith(".pdf"):
            original_file_path = os.path.join(input_folder, original_file)
            process_pdf(original_file_path, output_folder, config)
        
