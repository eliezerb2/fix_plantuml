"""
Main module for the fix_plantuml project.

This module processes command line parameters and invokes
the functions to remove adjacent duplicate lines and
remove linked attributes.
"""

import tempfile
import os
from src.param_processor import process_parameters
from src.remove_adjacent_duplicates import remove_adjacent_duplicates
from src.remove_linked_attributes import remove_linked_attributes


# Constants
TMP_FILE_PREFIX = 'fix_plantuml_'
TMP_FILE_SUFFIX = '.tmp'


def main() -> None:
    """
    Main function to execute the fix_plantuml program.
    It processes the command line parameters, removes adjacent
    duplicate lines, then removes linked attributes from the
    result, and ensures temporary files are handled correctly.
    """
    original_file_path, new_file_path, _ = process_parameters()

    # Create a temporary file for processing adjacent duplicates
    tmp_file = None
    try:
        tmp_file = tempfile.NamedTemporaryFile(
            prefix=TMP_FILE_PREFIX,
            suffix=TMP_FILE_SUFFIX,
            delete=False
        )
        tmp_file_path = tmp_file.name
        tmp_file.close()

        # Remove adjacent duplicate lines and write to the temporary file
        remove_adjacent_duplicates(original_file_path, tmp_file_path)

        # Remove linked attributes from the temporary file and write the result to a new file
        remove_linked_attributes(tmp_file_path, new_file_path)

    finally:
        # Ensure the temporary file is deleted
        if tmp_file_path and os.path.exists(tmp_file_path):
            try:
                os.remove(tmp_file_path)
            except OSError as e:
                print(f"Error deleting temporary file: {e}")


if __name__ == '__main__':
    main()
