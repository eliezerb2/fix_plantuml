"""
remove_linked_attributes.py

This module provides a function to remove class properties that are also declared
in a composition link from this class to another class in a PlantUML file.
"""

from typing import List, Dict

# Constants
COMPOSITION_SYMBOL = '--*'
ENCODING = 'utf-8'
CLASS_KEYWORD = 'class'


def remove_linked_attributes(input_file_path: str, output_file_path: str) -> None:
    """
    Removes class properties that are also declared in a composition link from this
    class to another class in a PlantUML file.

    :param input_file_path: Path to the input PlantUML file.
    :param output_file_path: Path to the output PlantUML file.
    :return: None
    """
    # Read the input file
    with open(input_file_path, 'r', encoding=ENCODING) as file:
        lines = file.readlines()

    # Parse the input file to find class definitions and composition links
    classes: Dict[str, List[str]] = {}
    compositions: Dict[str, List[str]] = {}

    current_class = None

    for line in lines:
        line = line.strip()

        # Identify class definitions
        if line.startswith(CLASS_KEYWORD):
            class_name = line.split()[1]
            current_class = class_name
            classes[current_class] = []

        # Identify class properties
        elif current_class and line.endswith(';'):
            property_name = line.split()[0]
            classes[current_class].append(property_name)

        # Identify composition links
        elif COMPOSITION_SYMBOL in line:
            class1, class2 = line.split(COMPOSITION_SYMBOL)
            class1, class2 = class1.strip(), class2.strip()
            if class1 not in compositions:
                compositions[class1] = []
            compositions[class1].append(class2)

    # Remove properties declared in composition links
    for class_name, linked_classes in compositions.items():
        if class_name in classes:
            for linked_class in linked_classes:
                if linked_class in classes:
                    linked_properties = set(classes[linked_class])
                    classes[class_name] = [prop for prop in classes[class_name] if prop not in linked_properties]

    # Write the result to the output file
    with open(output_file_path, 'w', encoding=ENCODING) as file:
        current_class = None
        for line in lines:
            stripped_line = line.strip()

            if stripped_line.startswith(CLASS_KEYWORD):
                class_name = stripped_line.split()[1]
                current_class = class_name
                file.write(line)

            elif current_class and stripped_line.endswith(';'):
                property_name = stripped_line.split()[0]
                if property_name not in classes[current_class]:
                    file.write(line)

            elif COMPOSITION_SYMBOL in stripped_line:
                file.write(line)

            else:
                file.write(line)
