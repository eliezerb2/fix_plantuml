"""
Module to remove adjacent duplicate lines from an unsorted text file.
"""


def remove_adjacent_duplicates(input_file_path: str, output_file_path: str) -> None:
    """
    Remove adjacent duplicate lines from an input file and write to an output file.

    Args:
        input_file_path (str): Path to the input file.
        output_file_path (str): Path to the output file.
    """
    # TODO: externalize the encoding to a parameter
    with open(input_file_path, 'r', encoding="utf-8") as infile, open(output_file_path, 'w', encoding="utf-8") as outfile:
        previous_line = None
        for line in infile:
            if line != previous_line:
                outfile.write(line)
                previous_line = line
