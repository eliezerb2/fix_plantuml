"""
This module provides a function to process PlantUML files by removing lines associated
with composition links and properties.
"""

from typing import Dict, List


# Initialize constants
ENCODING: str = 'utf-8'
CLASS_START_PREFIX: str = 'class '
CLASS_END: str = '}'
METHOD_SUFFIX: str = ')'
COMPOSITION_LINK_TYPE: str = '--*'
PROPERTY_SEPARATOR: str = ':'


def remove_linked_attributes(input_file_path: str, output_file_path: str) -> None:
    """
    Removes lines from a PlantUML file that are associated with composition links or properties.

    Args:
        input_file_path (str): The path to the input PlantUML file.
        output_file_path (str): The path to the output PlantUML file.

    Returns:
        None
    """

    # Initialize variables
    properties: Dict[str, int] = {}
    lines_to_remove: Dict[int, bool] = {}
    current_class: str = ""

    # Read lines from the input file
    with open(input_file_path, 'r', encoding=ENCODING) as file:
        lines: List[str] = file.readlines()

    for line_number, line in enumerate(lines):
        stripped_line: str = line.strip()

        # Split the line into parts
        parts: List[str] = stripped_line.split()

        # Class start
        if stripped_line.startswith(CLASS_START_PREFIX):
            class_name: str = parts[1].strip('"')
            current_class = class_name

        # Class end
        elif stripped_line.startswith(CLASS_END):
            current_class = ""

        # Property
        elif current_class and not stripped_line.endswith(METHOD_SUFFIX):
            property_name: str = parts[0]
            property_key: str = f"{current_class}{PROPERTY_SEPARATOR}{property_name}"
            properties[property_key] = line_number

        # Composition link
        elif COMPOSITION_LINK_TYPE in stripped_line:
            if len(parts) >= 5:
                src_class_property_key: str = f"{parts[2]}{PROPERTY_SEPARATOR}{parts[4]}"
                if src_class_property_key in properties:
                    # Mark property for removal
                    lines_to_remove[properties[src_class_property_key]] = True

    # Write lines to output file
    with open(output_file_path, 'w', encoding=ENCODING) as file:
        for line_number, line in enumerate(lines):
            if line_number not in lines_to_remove:
                file.write(line)
