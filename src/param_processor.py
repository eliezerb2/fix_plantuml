"""
Module to process command line parameters for the fix_plantuml project.

This module handles verifying the existence of the original file path,
determining the new file path, and confirming overwrites.
"""

import argparse
import os
import sys
import importlib.metadata


def get_version(project_name: str) -> str:
    """
    Retrieve the version number of the installed package using importlib.metadata.

    Args:
        project_name (str): The name of the project package.

    Returns:
        str: The version number of the package.

    Raises:
        RuntimeError: If the package version cannot be found.
    """
    try:
        return importlib.metadata.version(project_name)
    except importlib.metadata.PackageNotFoundError as exc:
        raise RuntimeError(f"The '{project_name}' package is not installed.") from exc


def process_parameters() -> tuple[str, str, str]:
    """
    Process and validate command line parameters.

    Returns:
        tuple: original file path, new file path, and confirmation flag.
    """
    parser = argparse.ArgumentParser(description="Process command line parameters.")
    parser.add_argument(
        "-o", "--original",
        # required=True,
        help="Original file path")
    parser.add_argument(
        "-n", "--new",
        required='--original' in sys.argv,
        help="New file path")
    parser.add_argument(
        "-c", "--confirm",
        choices=["y", "yes", "all"],
        help="Confirmation flag")
    parser.add_argument(
        '-v', '--version',
        action='store_true',
        help="Show the version of the program."
    )

    parsed_args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

    # Handle version display manually
    if parsed_args.version:
        version = get_version(parser.prog)
        print(f"{parser.prog} version {version}")
        sys.exit(0)

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
