"""
Module to process command line parameters for the fix_plantuml project.

This module handles verifying the existence of the original file path,
determining the new file path, and confirming overwrites.
"""

import argparse
import os


def process_parameters() -> tuple[str, str, str]:
    """
    Process and validate command line parameters.

    Returns:
        tuple: original file path, new file path, and confirmation flag.
    """
    parser = argparse.ArgumentParser(description="Process command line parameters.")
    parser.add_argument("--original", required=True, help="Original file path")
    parser.add_argument("--new", help="New file path")
    parser.add_argument("--confirm", choices=["y", "yes", "all"], help="Confirmation flag")

    parsed_args = parser.parse_args()
    original_file_path = parsed_args.original
    new_file_path = parsed_args.new if parsed_args.new else original_file_path
    confirm = parsed_args.confirm

    if not os.path.exists(original_file_path):
        raise FileNotFoundError(f"The original file path '{original_file_path}' does not exist.")

    if os.path.exists(new_file_path) and new_file_path != original_file_path and not confirm:
        response = input(f"The file '{new_file_path}' already exists. Overwrite? (y/n): ").strip().lower()
        if response not in ["y", "yes", "all"]:
            raise FileExistsError(f"The file '{new_file_path}' already exists and was not confirmed for overwrite.")

    return original_file_path, new_file_path, confirm
