# PDF Metadata Updater

This Python script updates the metadata of given PDF files. It creates 'output', 'input', and 'config' folders in the root directory to store the processed files.

## Author

Dennis Biehl

## License

MIT License

## Dependencies

- os
- PyPDF2
- configparser

## Usage

1. Ensure that PyPDF2 is installed using `pip install PyPDF2`.
2. Run the script by executing `start.py` to create 'output', 'input', and 'config' folders.
3. Place PDF files in the 'input' folder.
4. The script will merge each PDF's pages with its metadata and save the result in the 'output' folder.

## Functions

- `create_folders()`: Creates 'output', 'input', and 'config' folders if they don't exist and returns their paths.
- `create_config(config_file, config)`: Creates a configuration file with a 'Metadata' section.
- `update_config(config_file, config)`: Updates the configuration file with metadata values.
- `process_pdf(original_file_path, output_folder, config)`: Merges the pages of a PDF with its metadata and saves the result.

## Configuration

- The 'output', 'input', and 'config' folders are created in the root directory.
- Metadata such as Producer and Creator are set during the merging process.

## Version

1.0.0 (2024-01-14)

## Updates

- 2024-01-14: Initial release.

## Running the Script

Ensure Python is installed on your system, navigate to the root folder, and execute:

```bash
python start.py
```

## Note

- The script assumes a specific folder structure. Adjust paths if your project structure is different.
- Confirm PyPDF2 installation using `pip install PyPDF2` before running the script.
