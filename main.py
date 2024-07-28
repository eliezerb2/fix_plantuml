"""
Main module for the fix_plantuml project.

This module processes command line parameters and invokes the function to remove adjacent duplicate lines.
"""

from param_processor import process_parameters
from remove_adjacent_duplicates import remove_adjacent_duplicates


def main():
    """
    Main function to execute the fix_plantuml program.
    """
    original_file_path, new_file_path, _ = process_parameters()
    remove_adjacent_duplicates(original_file_path, new_file_path)


if __name__ == '__main__':
    main()
